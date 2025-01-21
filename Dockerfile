FROM python:3.11-slim-bullseye

# Install required system packages and tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev \
    default-mysql-client \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set timezone to Asia/Kolkata
RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

# Create necessary directories for logs and middleware
RUN mkdir -p /logs/middleware/

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Set working directory for the application
WORKDIR /usr/local/eka/middleware

# Copy requirements.txt and install Python dependencies
COPY ./requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt && rm requirements.txt

# Copy configuration files for uWSGI
COPY dockerconfig/uwsgi_middleware.ini /etc/uwsgi_middleware.ini

# Copy the application code
COPY ./middleware .

# Run collectstatic for Django to collect static files
RUN python3 manage.py collectstatic --noinput

# Expose port 80 for HTTP traffic
EXPOSE 80

# Create a non-root user and group
RUN groupadd -r ekacare && useradd -r -g ekacare ekacare

# Set ownership of application files to the non-root user
RUN chown -R ekacare:ekacare /usr/local/eka/middleware /logs/middleware

# Switch to the non-root user
USER ekacare

# Start uWSGI as the non-root user
CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi_middleware.ini"]
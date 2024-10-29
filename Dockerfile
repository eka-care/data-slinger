FROM python:3.11-slim-bullseye

# Install required system packages and tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev \
    default-mysql-client \
    pkg-config \
    curl \
    libaio1 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download the Oracle Instant Client (adjust URL for your version)
RUN curl -L -o instantclient-basic-linux.x64.zip \
    https://download.oracle.com/otn_software/linux/instantclient/2350000/instantclient-basic-linux.x64-23.5.0.24.07.zip

# Unzip and configure the Oracle Instant Client
RUN unzip instantclient-basic-linux.x64.zip -d /opt/oracle \
    && rm instantclient-basic-linux.x64.zip
RUN echo /opt/oracle/instantclient_21_1 > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

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
RUN python3 -m pip install -r requirements.txt

# Copy configuration files for uWSGI
COPY dockerconfig/uwsgi_middleware.ini /etc/uwsgi_middleware.ini

# Copy the application code
COPY ./middleware .

# Run collectstatic for Django to collect static files
RUN python3 manage.py collectstatic --noinput

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start uWSGI.
CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi_middleware.ini"]

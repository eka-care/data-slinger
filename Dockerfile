FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY .env .

RUN django-admin startproject webapp .

COPY otel.py ./webapp/
COPY wsgi.py ./webapp/

ENV DJANGO_SETTINGS_MODULE=webapp.settings

EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["uwsgi", "--http", ":8000", "--module", "webapp.wsgi:application"]
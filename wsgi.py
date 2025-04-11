"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
load_dotenv('/app/.env')

service_name = os.environ.get("SERVICENAME")

from .otel import initialize_telemetry
initialize_telemetry(service_name)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')



from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

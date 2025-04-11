"""
WSGI config for middleware project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

service_name = os.getenv("SERVICENAME")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'middleware.settings')

from .otel import initialize_telemetry
initialize_telemetry(service_name)

application = get_wsgi_application()


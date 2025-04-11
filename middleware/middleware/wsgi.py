"""
WSGI config for middleware project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .otel import initialize_telemetry

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'middleware.settings')

initialize_telemetry()

application = get_wsgi_application()


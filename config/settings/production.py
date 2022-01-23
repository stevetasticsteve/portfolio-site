from .base import *
import os

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY", "Secure_secret_key")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

# HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# EMAIL
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
NOCAPTCHA = True


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://9c2cc8540b8d426ab5de7989c4146d14@o538547.ingest.sentry.io/6160548",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
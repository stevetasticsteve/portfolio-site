from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-axrj7@fn9w2$-q)pcw)hsth(=ds&br_1(_iy66=%)p-*t^u+rb"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
NOCAPTCHA = True
RECAPTCHA_PUBLIC_KEY = "1"
RECAPTCHA_PRIVATE_KEY = "2"
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


try:
    from .local import *
except ImportError:
    pass

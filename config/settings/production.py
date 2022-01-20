from .base import *
import os

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY", "Secure_secret_key")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
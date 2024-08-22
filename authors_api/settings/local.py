from .base import *
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="uXKaUl_0zsklKgBpPjplhZ9GAFhbY2nt8iUU9c6U8rBFAF9Hf9c",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]



#seccccret key comand
#python -c "import secrets; print(secrets.token_urlsafe(38))"
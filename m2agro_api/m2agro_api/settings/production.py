# -*- coding: utf-8 -*-

u"""Production Settings of m2agro API."""

from .base import *

# Application definition

INSTALLED_APPS += [
]

MIDDLEWARE_CLASSES += [
]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

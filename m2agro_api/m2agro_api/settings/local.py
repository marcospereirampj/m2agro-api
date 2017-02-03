# -*- coding: utf-8 -*-

u"""Local Settings of m2agro API."""

from .base import *

# Debug

DEBUG = True

# Application definition

INSTALLED_APPS += [
]

MIDDLEWARE_CLASSES += [
]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'm2agro_db.db',
    }
}
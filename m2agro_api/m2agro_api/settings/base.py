# -*- coding: utf-8 -*-

u"""Base Settings of m2agro API."""

from os.path import abspath, dirname, join, normpath

# Server Configuration

BASE_DIR = dirname(dirname(abspath(__file__)))

SITE_ROOT = dirname(BASE_DIR)

SITE_ID = 2

# Debug

DEBUG = True

# Security

SECRET_KEY = 'k)npbjy$#3wp=r3k4877bfa&hrvcfad-!9%d=3z**7rfvutek-'

ALLOWED_HOSTS = ['*']

# Session

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 86400

# Database

DATABASES = {}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]

# Internationalization

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Maceio'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# URL end WSGI

ROOT_URLCONF = 'm2agro_api.urls'

WSGI_APPLICATION = 'm2agro_api.wsgi.application'

# Middlewares

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Base App

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'harvest'
]

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [normpath(join(SITE_ROOT, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
            'debug': DEBUG
        },
    },
]

# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = [
    normpath(join(SITE_ROOT, 'static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

MEDIA_URL = '/media/'
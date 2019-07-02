"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import datetime
import os
import dj_database_url

from .env import *


MINUTE = 60  # seconds

ADMINS = [
    ('Dan Starner', 'dstarner@bloomberg.net'),
    ('Ed Rhudy', 'erhudy@bloomberg.net'),
]

DEPLOY_ON_HEROKU = get_bool('DEPLOY_ON_HEROKU')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env('SECRET_KEY', '0=f(=4p68f$xr_-yo)(y&b0cv!uizr38-vk1-ju)f%6(=bmax$')

APPEND_SLASH = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_bool('DEBUG', True)

ALLOWED_HOSTS = get_list('ALLOWED_HOSTS', default=[])
if not DEBUG and not ALLOWED_HOSTS:
    raise ValueError("ALLOWED_HOSTS cannot be empty when not in DEBUG")

SECURE_SSL_REDIRECT = False

if not DEBUG:
    SECURE_HSTS_SECONDS = get_int('SECURE_HSTS_SECONDS', 60)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = get_bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', True)
    SECURE_CONTENT_TYPE_NOSNIFF = get_bool('SECURE_CONTENT_TYPE_NOSNIFF', True)
    SECURE_BROWSER_XSS_FILTER = get_bool('SECURE_BROWSER_XSS_FILTER', True)
    SECURE_SSL_REDIRECT = get_bool('SECURE_SSL_REDIRECT', True)
    SESSION_COOKIE_SECURE = get_bool('SESSION_COOKIE_SECURE', True)
    CSRF_COOKIE_SECURE = get_bool('CSRF_COOKIE_SECURE', True)
    SECURE_HSTS_PRELOAD = get_bool('SECURE_HSTS_PRELOAD', True)
    X_FRAME_OPTIONS = get_env('X_FRAME_OPTIONS', 'DENY').upper()

# Cors Configuration
CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_ORIGIN_WHITELIST = get_list('CORS_ORIGIN_WHITELIST', ['http://localhost:8080', 'http://127.0.0.1:8080'])

# Application definition
APP_ROOT = 'api.apps'

API_DOCS_NAME = 'docs'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_extensions',           # Provides extra functionality to manage.py
    'rest_framework',              # Provides all of the REST API functionality
    'storages',

    f'{APP_ROOT}.users',
    f'{APP_ROOT}.posts',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = f'/{API_DOCS_NAME}'

ROOT_URLCONF = 'api.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': get_path('db.sqlite3'),
    }
}

if DEPLOY_ON_HEROKU:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

USE_S3_STORAGE = get_bool('USE_S3_STORAGE')

AWS_ACCESS_KEY_ID = get_env('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = get_env('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = get_env('AWS_STORAGE_BUCKET_NAME', 'townvisor')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'api.config.storage_backends.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'api.config.storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'api.config.storage_backends.PrivateMediaStorage'

AWS_DEFAULT_ACL = 'public-read'

if not USE_S3_STORAGE:
    STATIC_URL = '/static/'
    STATIC_ROOT = get_path('static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = get_path('media')


# Application Logging
# https://docs.djangoproject.com/en/2.2/topics/logging/

LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'core_api': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}


# JWT Settings
# http://getblimp.github.io/django-rest-framework-jwt/#additional-settings

JWT_AUTH_EXPIRATION_MINUTES = get_int('JWT_AUTH_EXPIRATION_MINUTES', default=20)
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=JWT_AUTH_EXPIRATION_MINUTES * MINUTE),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}


# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # 'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    ),
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
}
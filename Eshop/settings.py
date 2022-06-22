"""
Django settings for Eshop project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime
import os
from pathlib import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^_g%33qd(g8bjc+*40&uh(ptgkb$&-*+0!i3$lu7xj1u166cbb'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL='store.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    "storages"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'store.middlewares.auth.auth_middleware'
]

ROOT_URLCONF = 'Eshop.urls'

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

WSGI_APPLICATION = 'Eshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "shopping",
        "USER": "admin",
        "HOST": 'shopping.c2ince2oewy3.us-east-1.rds.amazonaws.com',
        "PASSWORD": 'Chandelsaurav817',
        "PORT": '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if not DEBUG:
    print("________1_______")
    from Eshop.aws.conf import *

    # STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
    # MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
    # STATIC_URL = "/static_url/"
    # MEDIA_URL = "/media_url/"
    # STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_URL = "/image/download/"
    MEDIA_ROOT = BASE_DIR
    # STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_cdn"),)

AWS_STORAGE_BUCKET_NAME = "e-shop-django"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# MEDIA_URL = "/image/download/"
# MEDIA_ROOT = BASE_DIR
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_cdn"),)



STRIPE_SECRET_KEY="sk_test_51L3drLSBN7WqSIkpz3kKUoijl0LfxLBZTykfLr5GzN9rUooJKShWkpzJ4eaxzkZi8y6N4FVMSmifb7o9dntDHLAs00VMfsIqcE"
STRIPE_PUBLIC_KEY="pk_test_51L3drLSBN7WqSIkpYdOFdttKauIvhwSNhqZzqiTtVIOLKOR5Wobl3Uuk7P9cPDPya58ejgWWsXxjlOeulQBYy2rK00gPjOzpzU"
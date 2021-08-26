#!/usr/bin/env python

# This manage.py exists for the purpose of creating migrations
import sys

from django.conf import settings
from django.core.management import execute_from_command_line

settings.configure(
    ROOT_URLCONF="paypal.standard.ipn.tests.test_urls",
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "test.db",
        }
    },
    PAYPAL_IDENTITY_TOKEN="",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.admin",
        "django.contrib.contenttypes",
        "paypal.pro",
        "paypal.standard",
        "paypal.standard.ipn",
        "paypal.standard.pdt",
    ],
    CACHES={
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
            "TIMEOUT": 0,
            "KEY_PREFIX": "paypal_tests_",
        }
    },
    MIDDLEWARE_CLASSES=[],
    SECRET_KEY='required_by_django',
    MIDDLEWARE=[
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.request',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
)

if __name__ == "__main__":
    execute_from_command_line(sys.argv)

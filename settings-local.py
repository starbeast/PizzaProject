import logging
from PizzaProject.settings import *

DEBUG = True  # False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

ROOT_URLCONF = 'PizzaProject.urls'

MANAGERS = ADMINS

STRESS_TESTING = True

CSRF_COOKIE_SECURE = False

ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'bcdkey@gmail.com'
DOMAIN = "http://192.168.13.41:8010"

# set django-celery autoloader
import djcelery

djcelery.setup_loader()

"""
CREATE DATABASE PizzaProject CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'pyuser'@localhost IDENTIFIED BY 'welcome';
GRANT ALL PRIVILEGES ON `PizzaProject`.* TO `pyuser`@`localhost`;
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'PizzaProject',
        'USER': 'pyuser',
        'PASSWORD': 'welcome',
        'HOST': '',
        'PORT': '3306',
    }
}

#AWS_STORAGE_BUCKET_NAME = "nextcaller-qa"
#AWS_STORAGE_BUCKET_NAME = "nextcaller-qa"
#AWS_IS_GZIPPED = True
#AWS_S3_CUSTOM_DOMAIN = 'd20nedaeg9xo3x.cloudfront.net'
#
#STATIC_URL = '//d20nedaeg9xo3x.cloudfront.net/'
#STATICFILES_STORAGE = 'nextcaller.core.storage.S3PipelineStorage'
#

#Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 2000000, #~23 days (PyLibMCCache doesn't work properly with >30days timeout)
    }
}

#PIPELINE = True
#PIPELINE_AUTO = False
# if DEBUG:
#     # will output to your console
#     logging.basicConfig(
#         level = logging.DEBUG,
#         format = '%(asctime)s %(levelname)s %(message)s',
#         )

REALM = 'local'
ALLOWED_HOSTS = ['*']


# set information to connect to rabbitmq (broker)
BROKER_URL = "amqp://nc_user:nc_password@127.0.0.1:5672//ncvhost"

LOGGING['loggers'].update({
    'django.request': {
        'handlers': ['mail_admins'],
        'level': 'ERROR',
        'propagate': True,
    },
    'PizzaProject.custom': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
})


# from importlib import import_module
# patches = import_module('settings-patches')
# globals().update(patches.__dict__)

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'
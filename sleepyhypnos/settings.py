# -*- coding: utf-8 -*-
'''
Django settings for sleepyhypnos project

'''


import sys



DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('kk', 'fkfkbill@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# a redis db to serve captcha request and value pairs
CAPTCHA_REDIS = {
    "host":"localhost",
    "port":6379,
    "db":0,
}


# captcha config
# where captcha images files served
CAPTCHA_DIR=r"./captcha"
CAPTCHA_TTC=r"./fonts/wqy.ttc"
CHN_CHAR_TABLE_FILE="./test.txt"#r"./gb2312.txt"
CAPTCHA_CHAR_NUM=3
CAPTCHA_LINE=3


# default login url
LOGIN_URL="/log"


ALLOWED_HOSTS = ["*"]
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-CN'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    sys.path[0]+"/static",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'b=^w3&gs300sk$1q_#45!9dl#^zn(a6)1*z*k$f*yfk^pwp2^5'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    sys.path[0]+"/template",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    "hypnos",

    #put at the end
    "south",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

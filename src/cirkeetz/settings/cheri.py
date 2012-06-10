# -*- coding:utf-8 -*

from .common import *
import os

# ------------------------------------------------------------------------
# stuff that are not under revision control
# ------------------------------------------------------------------------
WORKSPACE_ROOT="/home/bruno/Work/projects/cirkeetz"
VAR_PATH = os.path.join(WORKSPACE_ROOT, "var")

# ------------------------------------------------------------------------
# usual stuff
# ------------------------------------------------------------------------
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('bruno', 'bruno.desthuilliers@gmail.com'),
    )

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'

# ------------------------------------------------------------------------
# Database
# ------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'cirkeetz',                    
        'USER': 'cirkeetz',                      
        'PASSWORD': 'cirkeetz',               
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
            },
        'HOST': '',                      
        'PORT': '',                      
        }
    }

# ------------------------------------------------------------------------
# PATH & URLS
# ------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(VAR_PATH, "media")
MEDIA_URL = '' # XXX dev server here, don't care

# ------------------------------------------------------------------------
# logging
# ------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            },
        },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
            },
        },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        },
    }


from .settings import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['*']

# Override DB settings here
"""
DATABASES = {

}
"""

# Enabling development apps
INSTALLED_APPS = INSTALLED_APPS + [
    'django_extensions',
    'debug_toolbar',
    'django_pdb',
]

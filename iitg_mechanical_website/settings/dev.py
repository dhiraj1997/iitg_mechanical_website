from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vx6haagw7!j)xp0ppc7vglyo2e$yddhxax*3_-jp=elru432(&'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

INTERNAL_IPS = ("172.16.72.8, 127.0.0.1, 0.0.0.0")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = INSTALLED_APPS + [
	'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE+[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

try:
    from .local import *
except ImportError:
    pass
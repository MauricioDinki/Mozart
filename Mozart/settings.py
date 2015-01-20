from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = os.environ.get("SECRET_KEY", None)

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'django_countries',
    'Thirdauth',
    'Works',
    'Profiles',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'Mozart.urls'

WSGI_APPLICATION = 'Mozart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH,'static'),
)

MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')
MEDIA_URL = '/media/'

THUMBNAIL_DEBUG = True


SUIT_CONFIG = {
    'ADMIN_NAME': 'Mozart',
}
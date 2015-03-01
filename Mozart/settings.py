from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = os.environ.get("SECRET_KEY", None)

DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH,'templates'),
)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'djangular',
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
    'social.apps.django_app.default',
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
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'Mozart.urls'

WSGI_APPLICATION = 'Mozart.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': os.environ.get("MOZART_DATABASE_NAME", None),
        'USER': os.environ.get("MOZART_DATABASE_USER", None),
        'PASSWORD': os.environ.get("MOZART_DATABASE_PASSWORD", None),
        'HOST': os.environ.get("MOZART_DATABASE_HOST", None),
        'PORT': os.environ.get("MOZART_DATABASE_PORT", None),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH,'static/dist'),
)

MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')
MEDIA_URL = '/media/'

THUMBNAIL_DEBUG = True

# Suit Configuration
SUIT_CONFIG = {
    'ADMIN_NAME': 'Mozart',
}

#Facebook Keys
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY", None)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET", None)

# Twitter Keys
SOCIAL_AUTH_TWITTER_KEY = os.environ.get("SOCIAL_AUTH_TWITTER_KEY", None)
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get("SOCIAL_AUTH_TWITTER_SECRET", None)

# Google Keys
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", None)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", None)

# Social Auth Pipeline
SOCIAL_AUTH_PIPELINE = (    
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'Thirdauth.pipeline.save_extra_params',
)

# Login Urls
LOGIN_REDIRECT_URL = 'work_list'
LOGIN_URL = 'login'
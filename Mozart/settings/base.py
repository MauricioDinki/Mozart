# -*- encoding: utf-8 -*-

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get("MOZART_SECRET_KEY", None)

ROOT_URLCONF = 'Mozart.urls'

WSGI_APPLICATION = 'Mozart.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 8,
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'Mozart',
    'MENU_ICONS': {
        'auth': 'icon-lock',
        'Events': 'icon-calendar',
        'Profiles': 'icon-user',
        'Thirdauth': 'icon-globe',
        'Works': 'icon-briefcase',
    },
}

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("MOZART_SOCIAL_AUTH_FACEBOOK_KEY", None)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("MOZART_SOCIAL_AUTH_FACEBOOK_SECRET", None)

SOCIAL_AUTH_TWITTER_KEY = os.environ.get("MOZART_SOCIAL_AUTH_TWITTER_KEY", None)
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get("MOZART_SOCIAL_AUTH_TWITTER_SECRET", None)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("MOZART_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", None)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("MOZART_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", None)

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

DISQUS_API_KEY = os.environ.get("DISQUS_API_KEY", None)
DISQUS_WEBSITE_SHORTNAME = os.environ.get("DISQUS_WEBSITE_SHORTNAME", None)

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", None)
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)

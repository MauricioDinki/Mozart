from base import *
import dj_database_url

DEBUG = False

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
    'rest_framework',
    'social.apps.django_app.default',
    'disqus',
    'Thirdauth',
    'Works',
    'Profiles',
    'Events',
    'storages',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/dist'),
)

STATIC_URL = "https://%s/" % os.environ.get("AWS_BUCKET_URL", None)

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

TEMPLATE_DEBUG = False

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

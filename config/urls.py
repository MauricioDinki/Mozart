# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from mozart.works import urls as works_urls
from mozart.landing import urls as landing_urls
from mozart.xauth import urls as xauth_urls
from mozart.profiles import urls as profiles_urls

urlpatterns = [
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('social.apps.django_app.urls', namespace='social')),

    # Your stuff: custom urls includes go here
    url(r'^', include(works_urls, namespace='works')),
    url(r'^', include(landing_urls, namespace='landing')),
    url(r'^', include(xauth_urls, namespace='xauth')),
    url(r'^', include(profiles_urls, namespace='profiles')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]

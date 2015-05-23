# -*- encoding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns,include,url
from django.contrib import admin
from rest_framework import routers
from API.viewsets import AddressViewSet, ContactViewSet, Date_of_BirthViewSet, EventViewSet, Mozart_UserViewSet, UserViewSet, WorkViewSet

router = routers.DefaultRouter()

router.register(r'mozart',Mozart_UserViewSet)
router.register(r'contact',ContactViewSet)
router.register(r'birth',Date_of_BirthViewSet)
router.register(r'users',UserViewSet)
router.register(r'worksets',WorkViewSet)
router.register(r'address',AddressViewSet)
router.register(r'events',EventViewSet)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-oauth/', include('rest_framework.urls',namespace = 'rest_framework')),
	url(r'^api/', include(router.urls)),
    url(r'', include('social.apps.django_app.urls', namespace = 'social')),

)

urlpatterns += patterns('',
    url(r'', include('Works.urls', namespace = u'works')),
    url(r'', include('Thirdauth.urls', namespace = u'thirdauth')),
    url(r'', include('Profiles.urls', namespace = u'profiles')),
    url(r'', include('Events.urls', namespace = u'events')),
)


urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,},name = 'media'),
)

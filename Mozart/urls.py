# -*- encoding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns,include,url
from django.contrib import admin
from Profiles.viewsets import UserViewSet,MozartUserViewSet,ContactViewSet,DateBirthViewSet,AdressViewSet
from rest_framework import routers
from Works.viewsets import WorkViewSet

router = routers.DefaultRouter()

# Profiles Modules
router.register(r'mozart_user',MozartUserViewSet)
router.register(r'user_contact',ContactViewSet)
router.register(r'user_dateofbirth',DateBirthViewSet)
router.register(r'users',UserViewSet)
router.register(r'worksets',WorkViewSet)
router.register(r'adress',AdressViewSet)


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

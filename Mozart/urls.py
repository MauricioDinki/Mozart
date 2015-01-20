from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from Profiles.viewsets import UserViewSet,MozartUserViewSet,SocialNetworkViewSet,ContactViewSet,DateBirthViewSet
from Works.viewsets import WorkViewSet

router = routers.DefaultRouter()

# Profiles Modules
router.register(r'mozart_user',MozartUserViewSet)
router.register(r'social_network',SocialNetworkViewSet)
router.register(r'user_contact',ContactViewSet)
router.register(r'user_dateofbirth',DateBirthViewSet)
router.register(r'users',UserViewSet)

# Works Module
router.register(r'works',WorkViewSet)


urlpatterns = patterns('',

    url(r'', include('Works.urls')),
    url(r'', include('Thirdauth.urls')),
    url(r'', include('Profiles.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-oauth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
)


if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,},name = 'media'),
	)
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
<<<<<<< HEAD
=======
from rest_framework import routers
from Profiles.views import UserViewSet,MozartUserViewSet,SocialNetworkViewSet,ContactViewSet,DateBirthViewSet
from Works.views import WorkViewSet

router = routers.DefaultRouter()

# Profiles Modules
router.register(r'mozart_user',MozartUserViewSet)
router.register(r'social_network',SocialNetworkViewSet)
router.register(r'user_contact',ContactViewSet)
router.register(r'user_dateofbirth',DateBirthViewSet)
router.register(r'users',UserViewSet)
>>>>>>> master

# Works Module
router.register(r'works',WorkViewSet)


urlpatterns = patterns('',
<<<<<<< HEAD
=======

    url(r'', include('Works.urls')),
    url(r'', include('Thirdauth.urls')),
    url(r'', include('Profiles.urls')),
)

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-oauth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
>>>>>>> master
)


if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,},name = 'media'),
	)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from Profiles.views import UserViewSet
from Works.views import WorkViewSet

router = routers.DefaultRouter()
router.register(r'works',WorkViewSet)
router.register(r'users',UserViewSet)

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Works.urls')),
    url(r'', include('Thirdauth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-oauth/', include('rest_framework.urls',namespace='rest_framework')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,},name = 'media'),
	)
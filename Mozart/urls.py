from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(
        template_name='bienvenida.html'),
        name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Works.urls')),
    url(r'', include('Thirdauth.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,},name = 'media'),
	)

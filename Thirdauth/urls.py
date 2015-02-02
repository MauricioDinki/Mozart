# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import LoginView,RegisterView

urlpatterns = patterns('',
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', 'Thirdauth.views.LogoutView', name='logout'),
	url(r'^registrarse/$', RegisterView.as_view(), name='register'),
	url(r'^social/$', 'Thirdauth.views.social_user', name='social'),
	url(r'^social/delete/(?P<uid>\w+)/$', 'Thirdauth.views.deletesocial', name='delete_social'),
)
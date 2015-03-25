# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url, include
from .views import LoginView, RegisterView

urlpatterns = patterns('',
	url(r'^login/$', LoginView.as_view(), name = 'login'),
	url(r'^logout/$', 'Thirdauth.views.LogoutView', name = 'logout'),
	url(r'^signup/$', RegisterView.as_view(), name = 'signup'),
)
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import LoginView

urlpatterns = patterns('',
	url(r'^login/$', LoginView.as_view(), name='login_view'),
	url(r'^logout/$', 'Thirdauth.views.LogoutView', name='logout_view'),
)
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
from .views import InformationFormView,ChangePasswordView

urlpatterns = patterns('',
	url(r'^settings/account', InformationFormView.as_view(), name='settings_account'),
	url(r'^settings/password', ChangePasswordView.as_view(), name='settings_password'),
)


#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^promoters/$', view=views.PromoterListView.as_view(), name='promoters_list'),
    url(regex=r'^settings/password/$', view=views.ChangePasswordView.as_view(), name='password_settings'),
    url(regex=r'^settings/account/$', view=views.ProfileSettingsView.as_view(), name='account_settings'),
    url(regex=r'^profiles/(?P<username>.*)/$', view=views.ProfileDetailView.as_view(), name='profile_detail'),
    url(regex=r'^settings/social/$', view=views.SocialNetworkSettingsView.as_view(), name='social_settings'),
    url(regex=r'^settings/social/(?P<provider>.*)/(?P<account_id>.*)/delete$', view=views.SocialNetworkDeleteView, name='social_delete'),
]

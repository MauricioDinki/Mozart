#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^login/$', view=views.LoginView.as_view(), name='login'),
    url(regex=r'^logout/$', view=views.LogoutView, name='logout'),
    url(regex=r'^signup/$', view=views.SignupView.as_view(), name='signup'),
]

#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^explore/$', view=views.WorkListView.as_view(), name='work_list'),
    url(regex=r'^explore/(?P<category>.*)/$', view=views.WorkListView.as_view(), name='work_list_category'),

    url(regex=r'^profiles/(?P<username>.*)/works/$', view=views.WorkUserView.as_view(), name='work_user_list'),
    url(regex=r'^profiles/(?P<username>.*)/works/(?P<slug>.*)/$', view=views.WorkDetailView.as_view(), name='worl_detail'),
    url(regex=r'^profiles/(?P<username>.*)/works/category/(?P<category>.*)/$', view=views.WorkUserView.as_view(), name='work_user_list_category'),

    url(regex=r'^settings/works/$', view=views.WorkSettingsView.as_view(), name='work_settings'),
    url(regex=r'^settings/works/(?P<slug>.*)/$', view=views.WorkUpdateView.as_view(), name='work_update'),

    url(regex=r'^works/create/$', view=views.WorkCreateView.as_view(), name='work_create'),
    url(regex=r'^works/delete/(?P<slug>.*)/$', view=views.WorkDeleteView, name='work_delete'),
]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^events/$', view=views.EventListView.as_view(), name='event_list'),
    url(regex=r'^events/create/$', view=views.EventCreateView.as_view(), name='event_create'),

    url(regex=r'^profiles/(?P<username>.*)/events/$', view=views.EventUserView.as_view(), name='event_user_list'),
]

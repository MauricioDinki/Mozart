#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^works/$', view=views.WorkList.as_view(), name='api_work_list'),
    url(regex=r'^events/$', view=views.EventList.as_view(), name='api_event_list'),
    url(regex=r'^extendeduser/$', view=views.ExtendedUserList.as_view(), name='api_extendeduser_list'),
    url(regex=r'^address/$', view=views.AddressList.as_view(), name='api_address_list'),
    url(regex=r'^contact/$', view=views.ContactList.as_view(), name='api_contact_list'),
    url(regex=r'^birthday/$', view=views.BirthdayList.as_view(), name='api_birthday_list'),
]

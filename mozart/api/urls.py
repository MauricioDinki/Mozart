#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^users/$', view=views.UserList.as_view(), name='api_user_list'),
    url(regex=r'^users/(?P<pk>[0-9]+)/$', view=views.UserDetail.as_view(), name='api_user_detail'),
    url(regex=r'^works/$', view=views.WorkList.as_view(), name='api_work_list'),
    url(regex=r'^works/(?P<pk>[0-9]+)/$', view=views.WorkDetail.as_view(), name='api_work_detail'),
    url(regex=r'^events/$', view=views.EventList.as_view(), name='api_event_list'),
    url(regex=r'^events/(?P<pk>[0-9]+)/$', view=views.EventDetail.as_view(), name='api_event_detail'),
    url(regex=r'^extendedusers/$', view=views.ExtendedUserList.as_view(), name='api_extendeduser_list'),
    url(regex=r'^extendedusers/(?P<pk>[0-9]+)/$', view=views.ExtendedUserDetail.as_view(), name='api_extendedusers_detail'),
    url(regex=r'^addresses/$', view=views.AddressList.as_view(), name='api_address_list'),
    url(regex=r'^addresses/(?P<pk>[0-9]+)/$', view=views.AddressDetail.as_view(), name='api_address_detail'),
    url(regex=r'^contacts/$', view=views.ContactList.as_view(), name='api_contact_list'),
    url(regex=r'^contacts/(?P<pk>[0-9]+)/$', view=views.ContactDetail.as_view(), name='api_contact_detail'),
    url(regex=r'^birthdays/$', view=views.BirthdayList.as_view(), name='api_birthday_list'),
    url(regex=r'^birthdays/(?P<pk>[0-9]+)/$', view=views.BirthdayDetail.as_view(), name='api_birthday_detail'),
    url(regex=r'^facebookauth/$', view=views.FacebookauthList.as_view(), name='api_facebookauth_list'),
    url(regex=r'^googleauth/$', view=views.GoogleauthList.as_view(), name='api_googleauth_list'),
    url(regex=r'^twitterauth/$', view=views.TwitterauthList.as_view(), name='api_twitterauth_list'),
]

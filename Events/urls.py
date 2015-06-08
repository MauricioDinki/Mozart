# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url, include

from Events.views import CreateEventView, ListEventView, UserEventView

urlpatterns = patterns(
    '',
    url(r'^profiles/(?P<username>.*)/events/$', UserEventView.as_view(), name='user_event_list'),
    url(r'^events/$', ListEventView.as_view(), name='event_list',),
    url(r'^create/event/$', CreateEventView.as_view(), name='create_event',),
)

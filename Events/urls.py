# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url,include
from .views import ListEventView

urlpatterns = patterns('',
	url(r'^events/$', ListEventView.as_view(), name = 'event_list',),
)
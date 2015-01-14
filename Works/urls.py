# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url,include
from .views import WorkListView, WorkDetailView,WorkViewSet
from rest_framework import routers

urlpatterns = patterns('',
	url(r'^explorar/$', WorkListView.as_view(), name='work_list'),
	url(r'^explorar/(?P<category>[\w\-]+)/$', WorkListView.as_view(), name='work_list_category'),
	url(r'^(?P<username>[\w\-]+)/obras/$', WorkListView.as_view(), name='work_user_list'),
	url(r'^(?P<username>[\w\-]+)/obras/(?P<slug>[\w\-]+)/$', WorkDetailView.as_view(), name='work_user_detail'),
)
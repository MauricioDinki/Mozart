# -*- encoding: utf-8 -*-

from .views import WorkListView, WorkDetailView, HomeView
from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index',),
	url(r'^explorar/$', WorkListView.as_view(), name='home'),
	url(r'^explorar/(?P<category>[\w\-]+)/$', WorkListView.as_view(), name='work_list_category'),
	url(r'^(?P<username>[\w\-]+)/obras/$', WorkListView.as_view(), name='work_user_list'),
	url(r'^(?P<username>[\w\-]+)/obras/(?P<slug>[\w\-]+)/$', WorkDetailView.as_view(), name='work_user_detail'),
)

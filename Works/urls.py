# -*- encoding: utf-8 -*-

# from .views import WorkListView, WorkDetailView, HomeView,UploadWorkView
from .views import WorkListView, HomeView, UploadWorkView, EditWorkView
from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index',),
	url(r'^create/work/$', UploadWorkView.as_view(), name='create_work'),
	url(r'^explore/$', WorkListView.as_view(), name='work_list'),
	url(r'^settings/works/(?P<slug>.*)/$', EditWorkView.as_view(), name='edit_work'),
	# url(r'^explore/(?P<category>[\w\-]+)/$', WorkListView.as_view(), name='work_list_category'),
	# url(r'^(?P<username>[\w\-]+)/works/$', WorkListView.as_view(), name='work_user_list'),
	# url(r'^(?P<username>[\w\-]+)/works/(?P<slug>[\w\-]+)/$', WorkDetailView.as_view(), name='work_user_detail'),
)

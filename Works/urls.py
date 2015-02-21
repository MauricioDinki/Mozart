# -*- encoding: utf-8 -*-

from .views import WorkListView, HomeView, UploadWorkView, WorkListUserView, EditWorkView, WorkUserView
from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index',),
	url(r'^create/work/$', UploadWorkView.as_view(), name='create_work'),
	url(r'^delete/work/(?P<slug>.*)/$','Works.views.DeleteWorkView', name='delete_work'),
	url(r'^explore/$', WorkListView.as_view(), name='work_list'),
	url(r'^explore/(?P<category>.*)/$', WorkListView.as_view(), name='work_list_category'),
	url(r'^settings/works/$', WorkListUserView.as_view(), name='settings_works'),
	url(r'^settings/works/(?P<slug>.*)/$', EditWorkView.as_view(), name='edit_work'),
	url(r'^(?P<username>.*)/works/(?P<slug>.*)/$', WorkUserView.as_view(), name='work_user_detail'),
)

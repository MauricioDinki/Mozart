# -*- encoding: utf-8 -*-

from .views import WorkListView, HomeView, WorkUploadView, WorkSettingsView, WorkEditView, WorkUserView, WorkUserDetailView
from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index',),
	url(r'^create/work/$', WorkUploadView.as_view(), name='create_work'),
	url(r'^delete/work/(?P<slug>.*)/$','Works.views.WorkDeleteView', name='delete_work'),
	url(r'^explore/$', WorkListView.as_view(), name='work_list'),
	url(r'^explore/(?P<category>.*)/$', WorkListView.as_view(), name='work_list_category'),
	url(r'^settings/works/$', WorkSettingsView.as_view(), name='settings_works'),
	url(r'^settings/works/(?P<slug>.*)/$', WorkEditView.as_view(), name='edit_work'),
	url(r'^(?P<username>.*)/works/(?P<slug>.*)/$', WorkUserDetailView.as_view(), name='work_user_detail'),
)

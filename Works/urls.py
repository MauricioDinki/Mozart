# -*- encoding: utf-8 -*-

from .views import ListWorkView, HomeView, CreateWorkView, SettingsWorkView, UpdateWorkView, UserWorkView, DetailWorkView, SearchProductsView
from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name = 'index',),
	url(r'^explore/$', ListWorkView.as_view(), name = 'work_list'),
	url(r'^explore/(?P<category>.*)/$', ListWorkView.as_view(), name = 'work_list_category'),
	url(r'^search/$', SearchProductsView.as_view(), name = 'search'),
)

urlpatterns += patterns('',
	url(r'^create/work/$', CreateWorkView.as_view(), name = 'create_work'),
	url(r'^delete/work/(?P<slug>.*)/$','Works.views.DeleteWorkView', name = 'delete_work'),
)

urlpatterns += patterns('',
	url(r'^settings/works/$', SettingsWorkView.as_view(), name = 'settings_works'),
	url(r'^settings/works/(?P<slug>.*)/$', UpdateWorkView.as_view(), name = 'edit_work'),
)

urlpatterns += patterns('',
	url(r'^profiles/(?P<username>.*)/works/category/(?P<category>.*)/$', UserWorkView.as_view(), name = 'work_user_list_category'),
	url(r'^profiles/(?P<username>.*)/works/(?P<slug>.*)/$', DetailWorkView.as_view(), name = 'work_user_detail'),
	url(r'^profiles/(?P<username>.*)/works/$', UserWorkView.as_view(), name = 'work_user_list'),	
)

	






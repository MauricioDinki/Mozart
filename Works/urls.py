from django.conf.urls import patterns, url
from .views import WorkListView

urlpatterns = patterns('',
	url(r'^explorar/$', WorkListView.as_view(), name='work_list'),
	url(r'^explorar/(?P<category>[\w\-]+)/$', WorkListView.as_view(), name='work_list'),
)
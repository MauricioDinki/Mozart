# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
from .views import InformationFormView

urlpatterns = patterns('',
	url(r'^configuracion/informacion', InformationFormView.as_view(), name='edit_information'),
)


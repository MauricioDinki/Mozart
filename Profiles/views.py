# -*- encoding: utf-8 -*-

from django.shortcuts import render,redirect
from rest_framework import viewsets
from .forms import UserInformationForm
from django.views.generic import FormView


class InformationFormView(FormView):
	template_name = 'edit-info.html'
	form_class = UserInformationForm
	success_url = '/explorar'

	def form_valid(self,form):
		return super(InformationFormView,self).form_valid(form)


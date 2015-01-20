# -*- encoding: utf-8 -*-

from django.shortcuts import render,redirect
from .forms import UserInformationForm
from django.views.generic import FormView
from django.core.urlresolvers import reverse

class InformationFormView(FormView):
	template_name = 'edit-info.html'
	form_class = UserInformationForm
	success_url = '/configuracion/informacion'

	def form_valid(self,form):
		return super(InformationFormView,self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super( InformationFormView,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

	def get_initial(self):

		initial={
			'day_of_birth':self.request.user.date_of_birth.day,
		}
		return initial



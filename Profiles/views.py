# -*- encoding: utf-8 -*-

from .forms import UserInformationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.views.generic import FormView

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
		initial = {
			'nationality':self.request.user.mozart_user.nationality
		}
		return initial



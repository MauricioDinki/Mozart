# -*- encoding: utf-8 -*-

from .forms import UserInformationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.views.generic import FormView

class InformationFormView(FormView):
	template_name = 'account-settings.html'
	form_class = UserInformationForm
	success_url = '/configuracion/informacion'

	def form_valid(self,form):
		form.save()
		return super(InformationFormView,self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super( InformationFormView,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

	def get_initial(self):
		initial = {
			'username' : self.request.user.username,
			'first_name':self.request.user.first_name,
			'last_name':self.request.user.last_name,
			'nationality':self.request.user.mozart_user.nationality,
			'description':self.request.user.mozart_user.description,
			'personal_homepage':self.request.user.contact.personal_homepage,
			'phone_number':self.request.user.contact.phone_number,
		}
		return initial



# -*- encoding: utf-8 -*-

from .forms import UserInformationForm,ChangePasswordForm
from .mixins import RequestFormMixin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView,View
from social.apps.django_app.default.models import UserSocialAuth
from Thirdauth.mixins import LoginRequiredMixin

class ChangePasswordView(LoginRequiredMixin,RequestFormMixin,FormView):
	template_name = 'settings-password.html'
	form_class = ChangePasswordForm
	success_url = reverse_lazy('index')

	def form_valid(self,form):
		form.save()
		logout(self.request)
		return super(ChangePasswordView,self).form_valid(form)

class InformationFormView(LoginRequiredMixin,RequestFormMixin,FormView):
	template_name = 'settings-account.html'
	form_class = UserInformationForm
	success_url =  reverse_lazy('settings_account')

	def form_valid(self,form):
		form.save()
		ctx = {'updated':'Perfil Actualizado','form':form}
		return render_to_response(self.template_name, ctx, context_instance = RequestContext(self.request))

	def get_initial(self):
		initial = {
			'adress':self.request.user.adress.adress,
			'city':self.request.user.adress.city,
			'description':self.request.user.mozart_user.description,
			'first_name':self.request.user.first_name,
			'last_name':self.request.user.last_name,
			'nationality':self.request.user.mozart_user.nationality,
			'neighborhood':self.request.user.adress.neighborhood,
			'personal_homepage':self.request.user.contact.personal_homepage,
			'profile_picture':self.request.user.mozart_user.profile_picture,
			'phone_number':self.request.user.contact.phone_number,
			'username' : self.request.user.username,
			'zip_code':self.request.user.adress.zip_code,
		}
		return initial


class SocialNetworkSettingsView(LoginRequiredMixin,View):
	template_name = 'settings-social.html'
	def get(self, request, *args, **kwargs):
		cuentas = UserSocialAuth.objects.filter(user__username = request.user.username)
		ctx = {'cuentas':cuentas}
		return render_to_response(self.template_name, ctx, context_instance = RequestContext(request))


@login_required(login_url='login')
def deleteSocialAccountView(request,provider,account_id):
	account_to_delete = UserSocialAuth.objects.get(user__username = request.user.username, provider = provider, id = account_id )
	account_to_delete.delete()
	return HttpResponseRedirect(reverse_lazy('settings_social'))


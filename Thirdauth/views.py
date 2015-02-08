# -*- encoding: utf-8 -*-

from .forms import LoginForm,RegisterForm
from .mixins import AuthRedirectMixin,LoginRequiredMixin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.views.generic import FormView,View
from social.apps.django_app.default.models import UserSocialAuth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy


class LoginView(AuthRedirectMixin,FormView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url =  reverse_lazy('work_list')

	def form_valid(self,form):
		login(self.request,form.user_cache)
		return super(LoginView,self).form_valid(form)

@login_required(login_url='login')
def LogoutView(request):
	logout(request)
	return redirect('index')

class RegisterView(AuthRedirectMixin,FormView):
	template_name = 'registro.html'
	form_class = RegisterForm
	success_url =  reverse_lazy('work_list')

	def form_valid(self,form):
		form.save()
		login(self.request,form.user_cache)
		return super(RegisterView,self).form_valid(form)

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
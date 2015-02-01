# -*- encoding: utf-8 -*-

from .forms import LoginForm,RegisterForm
from .mixins import AuthRedirectMixin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.views.generic import FormView

class LoginView(FormView):
	template_name = 'login-form.html'
	form_class = LoginForm
	success_url = '/explorar'

	def form_valid(self,form):
		login(self.request,form.user_cache)
		return super(LoginView,self).form_valid(form)

@login_required(login_url='login_view')
def LogoutView(request):
	logout(request)
	return redirect('home')

class RegisterView(AuthRedirectMixin,FormView):
	template_name = 'registro.html'
	form_class = RegisterForm
	success_url = '/success'

	def form_valid(self,form):
		form.save()
		login(self.request,form.user_cache)
		return super(RegisterView,self).form_valid(form)


from social.apps.django_app.default.models import UserSocialAuth
from django.template import RequestContext
from Profiles.models import Mozart_User

def social_user(request):
	template = 'socialCuenta.html'
	cuentas = UserSocialAuth.objects.filter(user__username = request.user.username)
	ctx = {'cuentas':cuentas}
	return render_to_response(template, ctx, context_instance = RequestContext(request))

def deletesocial(request):
	pass
	

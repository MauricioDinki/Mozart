# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import login,logout
from django.views.generic import FormView
from .forms import LoginForm,RegisterForm
from .mixins import AuthRedirectMixin
from django.contrib.auth.decorators import login_required


class LoginView(AuthRedirectMixin,FormView):
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


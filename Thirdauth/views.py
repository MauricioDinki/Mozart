# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import login,logout
from django.views.generic import FormView
from .forms import LoginForm

class LoginView(FormView):
	template_name = 'login-form.html'
	form_class = LoginForm
	success_url = '/explorar'

	def form_valid(self,form):
		login(self.request,form.user_cache)
		return super(LoginView,self).form_valid(form)

def LogoutView(request):
	logout(request)
	return redirect('work_list')


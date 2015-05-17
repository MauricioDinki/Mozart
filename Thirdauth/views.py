# -*- encoding: utf-8 -*-

from .forms import LoginForm,RegisterForm
from .mixins import AuthRedirectMixin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView,View


class LoginView(AuthRedirectMixin,FormView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url =  reverse_lazy('works:work_list')

	def form_valid(self,form):
		login(self.request,form.user_cache)
		return super(LoginView,self).form_valid(form)

	def get_context_data(self, **kwargs):
	    context = super(LoginView, self).get_context_data(**kwargs)
	    context.update(form=LoginForm())
	    return context


class RegisterView(AuthRedirectMixin,FormView):
	template_name = 'signup.html'
	form_class = RegisterForm
	success_url =  reverse_lazy('works:work_list')

	def form_valid(self,form):
		form.save()
		login(self.request,form.user_cache)
		return super(RegisterView,self).form_valid(form)
	
	def get_context_data(self, **kwargs):
	    context = super(RegisterView, self).get_context_data(**kwargs)
	    context.update(form=RegisterForm())
	    return context


@login_required(login_url='login')
def LogoutView(request):
	logout(request)
	return redirect('works:index')

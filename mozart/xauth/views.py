#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from mozart.core.mixins import AuthRedirectMixin

from .forms import LoginForm, SignupForm


class LoginView(AuthRedirectMixin, FormView):
    template_name = 'xauth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('works:work_list')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)


@login_required(login_url='login')
def LogoutView(request):
    logout(request)
    return redirect('landing:home')


class SignupView(AuthRedirectMixin, FormView):
    # template_name = 'xauth/signup.html'
    template_name = 'generic-form.html'
    form_class = SignupForm
    success_url = reverse_lazy('works:work_list')

    def form_valid(self, form):
        form.save()
        login(self.request, form.user_cache)
        return super(SignupView, self).form_valid(form)

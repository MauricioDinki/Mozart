# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from rest_framework import serializers


class AuthRedirectMixin(object):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('works:work_list')
        else:
            return super(AuthRedirectMixin, self).get(self, request, *args, **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class RequestFormMixin(object):
    def get_form_kwargs(self):
        kwargs = super(RequestFormMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

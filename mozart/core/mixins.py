#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class AuthRedirectMixin(object):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('works:work_list')
        else:
            return super(AuthRedirectMixin, self).get(self, request, *args, **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('xauth:login')))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class RequestFormMixin(object):
    def get_form_kwargs(self):
        kwargs = super(RequestFormMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class SuccessMessage(object):
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(SuccessMessage, self).form_valid(form)

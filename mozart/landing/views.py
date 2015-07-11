#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from mozart.core.mixins import AuthRedirectMixin


class HomeTemplateView(AuthRedirectMixin, TemplateView):
    template_name = 'pages/home.html'

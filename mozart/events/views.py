#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.http import Http404

from mozart.core.mixins import RequestFormMixin
from mozart.core.messages import not_found_messages

from .forms import EventCreateForm


class EventListView(TemplateView):
    template_name = 'events/event_list.html'


class CreateEventView(RequestFormMixin, CreateView):
    form_class = EventCreateForm
    success_url = reverse_lazy('events:event_list')
    template_name = 'events/create_event.html'


class EventUserView(TemplateView):
    template_name = 'events/event_user_list.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['username'] = self.kwargs.get('username')
            try:
                User.objects.get(username__iexact=self.kwargs.get('username'))
            except User.DoesNotExist:
                raise Http404(not_found_messages['404_user'])
        return kwargs

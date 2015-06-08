# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, TemplateView
from django.contrib.auth.models import User

from Events.forms import CreateEventForm, current_date
from Events.models import Event
from Utils.mixins import RequestFormMixin


class ListEventView(ListView):
    template_name = "event_list.html"
    queryset = Event.objects.all()
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super(ListEventView, self).get_context_data(**kwargs)
        context.update({'current_date': current_date})
        return context


class CreateEventView(RequestFormMixin, FormView):
    form_class = CreateEventForm
    success_url = reverse_lazy('events:event_list')
    template_name = 'create_event.html'

    def form_valid(self, form):
        form.save()
        return super(CreateEventView, self).form_valid(form)


class UserEventView(TemplateView):
    template_name = "event_user.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['username'] = self.kwargs.get('username')
            user = get_object_or_404(User, username__iexact=self.kwargs.get('username'))
        return kwargs

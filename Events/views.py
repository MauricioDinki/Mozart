# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, FormView

from Events.forms import CreateEventForm
from Events.models import Event
from Utils.mixins import RequestFormMixin


class ListEventView(ListView):
    template_name = "event_list.html"
    queryset = Event.objects.all()
    context_object_name = 'events'


class CreateEventView(RequestFormMixin, FormView):
    form_class = CreateEventForm
    success_url = reverse_lazy('events:event_list')
    template_name = 'create_event.html'
    # template_name = 'generic-form.html'

    def form_valid(self, form):
        form.save()
        return super(CreateEventView, self).form_valid(form)

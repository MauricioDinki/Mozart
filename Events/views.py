from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import CreateEventForm
from .models import Event
from django.core.urlresolvers import reverse_lazy

class ListEventView(TemplateView):
    template_name = "event_list.html"

class CreateEventView(FormView):
	form_class = CreateEventForm
	success_url =  reverse_lazy('events:event_list')
	template_name = 'generic-form.html'
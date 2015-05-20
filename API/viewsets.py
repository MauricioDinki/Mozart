# -*- encoding: utf-8 -*-

from .filters import EventFilter
from .serializers import EventSerializer
from Events.models import Event
from rest_framework import viewsets
from django_filters import filters

class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_class = EventFilter
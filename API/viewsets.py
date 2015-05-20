# -*- encoding: utf-8 -*-

from .filters import AdressFilter, ContactFilter, Date_of_BirthFilter, EventFilter, WorkFilter
from .serializers import AdressSerializer, ContactSerializer, Date_of_BirthSerializer, EventSerializer, UserSerializer, WorkSerializer
from django.contrib.auth.models import User
from django_filters import filters
from Events.models import Event
from Profiles.models import Adress, Contact, Date_of_Birth
from rest_framework import viewsets
from Works.models import Work

class AdressViewSet(viewsets.ModelViewSet):
	queryset = Adress.objects.all()
	serializer_class = AdressSerializer
	filter_class = AdressFilter

class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	filter_class = ContactFilter

class Date_of_BirthViewSet(viewsets.ModelViewSet):
	queryset = Date_of_Birth.objects.all()
	serializer_class = Date_of_BirthSerializer
	filter_class = Date_of_BirthFilter

class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_class = EventFilter

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_fields = ('username',)

class WorkViewSet(viewsets.ModelViewSet):
	queryset = Work.objects.all()
	serializer_class = WorkSerializer
	filter_class = WorkFilter
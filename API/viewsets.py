# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django_filters import filters

from rest_framework import viewsets

from API.filters import AddressFilter, ContactFilter, Date_of_BirthFilter, EventFilter, Mozart_UserFilter, WorkFilter
from API.serializers import AddressSerializer, ContactSerializer, Date_of_BirthSerializer, EventSerializer, Mozart_UserSerializer, UserSerializer, WorkSerializer
from Events.models import Event
from Profiles.models import Address, Contact, Date_of_Birth, Mozart_User
from Works.models import Work


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_class = AddressFilter


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


class Mozart_UserViewSet(viewsets.ModelViewSet):
    queryset = Mozart_User.objects.all()
    serializer_class = Mozart_UserSerializer
    filter_class = Mozart_UserFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username',)


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_class = WorkFilter

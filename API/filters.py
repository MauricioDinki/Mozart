# -*- encoding: utf-8 -*-

from Events.models import Event
from rest_framework import generics
from Profiles.models import Adress, Contact, Date_of_Birth
from Works.models import Work
import django_filters

class AdressFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name = "user__username")
    class Meta:
        model = Adress
        fields = ['user']
        order_by = ['user']

class ContactFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name = "user__username")
    class Meta:
        model = Contact
        fields = ['user']
        order_by = ['user']

class Date_of_BirthFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name = "user__username")
    class Meta:
        model = Date_of_Birth
        # fields = ['user']
        # order_by = ['user'] 

class EventFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name = "user__username")
    class Meta:
        model = Event
        fields = ['user', 'date',]
        order_by = ['-date']


class WorkFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name = "user__username")
    class Meta:
        model = Work
        fields = ['user', 'category', 'work_type']
        order_by = ['-date']

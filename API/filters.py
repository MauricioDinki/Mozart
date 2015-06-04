# -*- encoding: utf-8 -*-

from Events.models import Event
from rest_framework import generics
from Profiles.models import Address, Contact, Date_of_Birth, Mozart_User
from Works.models import Work
import django_filters


class GenericUserFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name="user__username")

    class Meta:
        fields = ['user']
        order_by = ['user']


class AddressFilter(GenericUserFilter):

    class Meta:
        model = Address


class ContactFilter(GenericUserFilter):

    class Meta:
        model = Contact


class Date_of_BirthFilter(GenericUserFilter):

    class Meta:
        model = Date_of_Birth


class EventFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name="user__username")

    class Meta:
        model = Event
        fields = ['user', 'date']
        order_by = ['-date']


class Mozart_UserFilter(GenericUserFilter):
    user = django_filters.CharFilter(name="user__username")

    class Meta:
        model = Mozart_User
        fields = ['user', 'sex', 'nationality', 'user_type']


class WorkFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name="user__username")

    class Meta:
        model = Work
        fields = ['user', 'category', 'work_type', 'slug']
        order_by = ['-date']

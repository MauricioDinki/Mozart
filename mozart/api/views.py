#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters

from mozart.works.models import Work
from mozart.events.models import Event
from mozart.profiles.models import Address, Contact, Birthday, ExtendedUser

from . import serializers
from . import filters as mz_filters


class WorkList(generics.ListCreateAPIView):
    serializer_class = serializers.WorkSerializer
    queryset = Work.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = mz_filters.WorkFilter


class EventList(generics.ListCreateAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = mz_filters.EventFilter


class AddressList(generics.ListCreateAPIView):
    serializer_class = serializers.AddressSerializer
    queryset = Address.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = mz_filters.AddressFilter


class ContactList(generics.ListCreateAPIView):
    serializer_class = serializers.ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = mz_filters.ContactFilter


class BirthdayList(generics.ListCreateAPIView):
    serializer_class = serializers.BirthdaySerializer
    queryset = Birthday.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = mz_filters.BirthdayFilter


class ExtendedUserList(generics.ListCreateAPIView):
    serializer_class = serializers.ExtendedUserSerializer
    queryset = ExtendedUser.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = mz_filters.ExtendedUserFilter

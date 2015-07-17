#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import serializers

from mozart.events.models import Event
from mozart.profiles.models import Address, Contact, Birthday, ExtendedUser
from mozart.works.models import Work


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Address
        exclude = ['url']


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Contact
        exclude = ['url']


class BirthdaySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Birthday
        exclude = ['url']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Event
        fields = ('cover', 'date', 'description', 'finish_time', 'name', 'place', 'slug', 'start_time', 'user',)


class ExtendedUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = ExtendedUser
        exclude = ['url']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'date_joined', 'first_name', 'last_name', 'email')


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Work
        fields = ('title', 'slug', 'date', 'description', 'category', 'cover', 'archive', 'work_type', 'user')

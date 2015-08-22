#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import serializers

from mozart.events.models import Event
from mozart.profiles.models import Address, Contact, Birthday, ExtendedUser, \
    Facebookauth, Googleauth, Twitterauth
from mozart.works.models import Work

from .mixins import GenericSocialSerializer


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Address
        fields = ('id', 'user', 'address', 'city', 'zip_code', 'neighborhood')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Contact
        fields = ('id', 'user', 'personal_homepage', 'phone_number')


class BirthdaySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Birthday
        fields = ('id', 'user', 'day', 'month', 'year')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Event
        fields = ('id', 'cover', 'date', 'description', 'finish_time', 'name', 'place', 'slug', 'start_time', 'user',)


class ExtendedUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = ExtendedUser
        fields = ('id', 'user', 'description', 'nationality', 'presentation_file', 'profile_picture', 'sex', 'user_type')


class FacebookauthSerializer(GenericSocialSerializer):
    class Meta(GenericSocialSerializer.Meta):
        model = Facebookauth


class GoogleauthSerializer(GenericSocialSerializer):
    class Meta(GenericSocialSerializer.Meta):
        model = Googleauth


class TwitterauthSerializer(GenericSocialSerializer):
    class Meta(GenericSocialSerializer.Meta):
        model = Twitterauth


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'date_joined', 'first_name', 'last_name', 'email')


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Work
        fields = ('id', 'title', 'slug', 'date', 'description', 'category', 'cover', 'archive', 'work_type', 'user')

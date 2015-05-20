# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from Events.models import Event
from Profiles.models import Adress, Contact, Date_of_Birth
from rest_framework import serializers
from Utils.mixins import UsernameSerializerMixin
from Works.models import Work

class AdressSerializer(UsernameSerializerMixin, serializers.HyperlinkedModelSerializer):
	user = UsernameSerializerMixin.user
	class Meta:
		model = Adress
		exclude = ['url']

class ContactSerializer(UsernameSerializerMixin, serializers.HyperlinkedModelSerializer):
	user = UsernameSerializerMixin.user
	class Meta:
		model = Contact
		exclude = ['url']

class Date_of_BirthSerializer(UsernameSerializerMixin, serializers.HyperlinkedModelSerializer):
	user = UsernameSerializerMixin.user
	class Meta:
		model = Date_of_Birth
		exclude = ['url']

class EventSerializer(UsernameSerializerMixin, serializers.HyperlinkedModelSerializer):
	user = UsernameSerializerMixin.user
	class Meta:
		model = Event
		fields = ('cover', 'date', 'description', 'finish_time', 'name', 'place', 'slug', 'start_time', 'user',)


class WorkSerializer(UsernameSerializerMixin, serializers.HyperlinkedModelSerializer):
	user = UsernameSerializerMixin.user
	class Meta:
		model = Work
		fields = ('title', 'slug', 'date', 'description', 'category', 'cover', 'archive', 'work_type', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username','date_joined','first_name','last_name', 'email')


# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from Events.models import Event
from Profiles.models import Adress, Contact, Date_of_Birth, Mozart_User
from rest_framework import serializers
from Works.models import Work

class AdressSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Adress
		exclude = ['url']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Contact
		exclude = ['url']

class Date_of_BirthSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Date_of_Birth
		exclude = ['url']

class EventSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Event
		fields = ('cover', 'date', 'description', 'finish_time', 'name', 'place', 'slug', 'start_time', 'user',)


class Mozart_UserSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Mozart_User
		exclude = ['url']

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username','date_joined','first_name','last_name', 'email')

class WorkSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Work
		fields = ('title', 'slug', 'date', 'description', 'category', 'cover', 'archive', 'work_type', 'user')




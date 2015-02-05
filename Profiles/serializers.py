# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Social_Network_URL,Date_of_Birth
from django.contrib.auth.models import User
from rest_framework import serializers

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact

class DateBirthSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Date_of_Birth

class MozartUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mozart_User

class SocialNetworkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Social_Network_URL

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email',)


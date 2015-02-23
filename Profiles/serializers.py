# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Date_of_Birth
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username','date_joined','first_name','last_name','email')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
	class Meta:
		model = Contact
		exclude = ['url']

class DateBirthSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
	class Meta:
		model = Date_of_Birth
		exclude = ['url']

class MozartUserSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
	class Meta:
		model = Mozart_User
		exclude = ['url']

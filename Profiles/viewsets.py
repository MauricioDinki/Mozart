# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Social_Network_URL,Date_of_Birth
from .serializers import UserSerializer,ContactSerializer,DateBirthSerializer,SocialNetworkSerializer,MozartUserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

class ContactViewSet(viewsets.ModelViewSet):
	model = Contact
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

class DateBirthViewSet(viewsets.ModelViewSet):
	model = Date_of_Birth
	queryset = Date_of_Birth.objects.all()
	serializer_class = DateBirthSerializer

class MozartUserViewSet(viewsets.ModelViewSet):
	model = Mozart_User
	queryset = Mozart_User.objects.all()
	serializer_class = MozartUserSerializer

class SocialNetworkViewSet(viewsets.ModelViewSet):
	model = Social_Network_URL
	queryset = Social_Network_URL.objects.all()
	serializer_class = SocialNetworkSerializer

class UserViewSet(viewsets.ModelViewSet):
	model = User
	queryset = User.objects.all()
	serializer_class = UserSerializer
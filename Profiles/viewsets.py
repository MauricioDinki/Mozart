# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Date_of_Birth
from .serializers import UserSerializer,ContactSerializer,DateBirthSerializer,MozartUserSerializer
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

class UserViewSet(viewsets.ModelViewSet):
	model = User
	queryset = User.objects.all()
	serializer_class = UserSerializer
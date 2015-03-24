# -*- encoding: utf-8 -*-

from .mixins import FilterUsernameMixin
from .models import Mozart_User,Contact,Date_of_Birth,Adress
from .serializers import UserSerializer,ContactSerializer,DateBirthSerializer,MozartUserSerializer,AdressSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

class AdressViewSet(FilterUsernameMixin, viewsets.ModelViewSet):
	queryset = Adress.objects.all()
	serializer_class = AdressSerializer

class ContactViewSet(FilterUsernameMixin, viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer


class DateBirthViewSet(FilterUsernameMixin, viewsets.ModelViewSet):
	queryset = Date_of_Birth.objects.all()
	serializer_class = DateBirthSerializer


class MozartUserViewSet(FilterUsernameMixin, viewsets.ModelViewSet):
	queryset = Mozart_User.objects.all()
	serializer_class = MozartUserSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_queryset(self):
		username = self.request.query_params.get('username')
		paginate = self.request.query_params.get('paginate')
		if username is not None:
			queryset = self.queryset.filter(username = username)[:paginate]
		else:
			queryset = self.queryset
		return queryset
# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Date_of_Birth
from .serializers import UserSerializer,ContactSerializer,DateBirthSerializer,MozartUserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .mixins import FilterUsernameMixin

class ContactViewSet(FilterUsernameMixin,viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	def get_queryset(self):
		username = self.request.query_params.get('username', None)
		paginate = self.request.query_params.get('paginate')
		if username is not None:
			queryset = self.queryset.filter(user__username = username)[:paginate]
		else:
			queryset = self.queryset
		return queryset

class DateBirthViewSet(FilterUsernameMixin,viewsets.ModelViewSet):
	queryset = Date_of_Birth.objects.all()
	serializer_class = DateBirthSerializer
	def get_queryset(self):
		username = self.request.query_params.get('username', None)
		paginate = self.request.query_params.get('paginate')
		if username is not None:
			queryset = self.queryset.filter(user__username = username)[:paginate]
		else:
			queryset = self.queryset
		return queryset

class MozartUserViewSet(FilterUsernameMixin,viewsets.ModelViewSet):
	queryset = Mozart_User.objects.all()
	serializer_class = MozartUserSerializer

	def get_queryset(self):
		username = self.request.query_params.get('username', None)
		paginate = self.request.query_params.get('paginate')
		if username is not None:
			queryset = self.queryset.filter(user__username = username)[:paginate]
		else:
			queryset = self.queryset
		return queryset

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
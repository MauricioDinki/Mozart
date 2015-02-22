# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Date_of_Birth
from .serializers import UserSerializer,ContactSerializer,DateBirthSerializer,MozartUserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .mixins import FilterUsernameMixin

class ContactViewSet(FilterUsernameMixin,viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

class DateBirthViewSet(FilterUsernameMixin,viewsets.ModelViewSet):
	queryset = Date_of_Birth.objects.all()
	serializer_class = DateBirthSerializer

class MozartUserViewSet(FilterUsernameMixin,viewsets.ModelViewSet):
	queryset = Mozart_User.objects.all()
	serializer_class = MozartUserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_queryset(self):
		author = self.request.query_params.get('author')
		paginate = self.request.query_params.get('paginate')
		if author is not None:
			queryset = self.queryset.filter(username = author)[:paginate]
		else:
			queryset = self.queryset
		return queryset
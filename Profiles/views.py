# -*- encoding: utf-8 -*-

from .models import Mozart_User,Contact,Social_Network,Date_of_Birth
from .serializers import UserSerializer,ContactSerializer,DateBirthSerializer,SocialNetworkSerializer,MozartUserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from rest_framework import viewsets
from .forms import UserInformationForm
from django.views.generic import FormView


class InformationFormView(FormView):
	template_name = 'edit-info.html'
	form_class = UserInformationForm
	success_url = '/explorar'

	def form_valid(self,form):
		return super(InformationFormView,self).form_valid(form)


# Vistas Del API REST

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
	model = Social_Network
	queryset = Social_Network.objects.all()
	serializer_class = SocialNetworkSerializer

class UserViewSet(viewsets.ModelViewSet):
	model = User
	queryset = User.objects.all()
	serializer_class = UserSerializer

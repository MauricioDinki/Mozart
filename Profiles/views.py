from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

# Vistas Del API REST

class UserViewSet(viewsets.ModelViewSet):
	model = User
	queryset = User.objects.all()
	serializer_class = UserSerializer 
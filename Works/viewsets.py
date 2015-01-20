# -*- encoding: utf-8 -*-
from rest_framework import viewsets
from .serializers import WorkSerializer
from .models import Work

class WorkViewSet(viewsets.ModelViewSet):
	model = Work
	queryset = Work.objects.all()
	serializer_class = WorkSerializer 
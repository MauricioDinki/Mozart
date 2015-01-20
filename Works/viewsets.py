# -*- encoding: utf-8 -*-

from .models import Work
from .serializers import WorkSerializer
from rest_framework import viewsets

class WorkViewSet(viewsets.ModelViewSet):
	model = Work
	queryset = Work.objects.all()
	serializer_class = WorkSerializer 
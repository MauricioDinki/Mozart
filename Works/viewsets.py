# -*- encoding: utf-8 -*-

from .models import Work
from .serializers import WorkSerializer
from rest_framework import viewsets

class WorkViewSet(viewsets.ModelViewSet):
	serializer_class = WorkSerializer 
	queryset = Work.objects.all()

	def get_queryset(self):
		category = self.request.query_params.get('category',None)
		author = self.request.query_params.get('author',None)
		paginate = self.request.query_params.get('paginate',None)
		if category is not None:
			if category == 'all':
				queryset = Work.objects.all()[:paginate]
			queryset = self.queryset.filter(category = category)[:paginate]
		elif author is not None:
			queryset = self.queryset.filter(user__username = author)[:paginate]
		elif paginate is not None:
			queryset = Work.objects.all()[:paginate]
		else:
			queryset = self.queryset
		return queryset
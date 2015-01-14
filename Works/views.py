# -*- encoding: utf-8 -*-

from .models import Work
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404
from django.views.generic import ListView,DetailView
from rest_framework import viewsets
from .serializers import WorkSerializer

class WorkListView(ListView):
    model = Work

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        data = [{
	        'user': Work.user.username,
	        'title':Work.title,
	        'category':Work.category,
	        'date':Work.date,
	        'cover':Work.cover.url,
	        'archive':Work.archive.url,
        } for Work in self.object_list]
    	return JsonResponse(data,safe=False)

    def get_queryset(self):
        if self.kwargs.get('category'):
            queryset = get_list_or_404(self.model,category=self.kwargs['category'])
       	elif self.kwargs.get('username'):
   			queryset = get_list_or_404(self.model,user__username__iexact=self.kwargs['username'])
        else:
            queryset = super(WorkListView, self).get_queryset()
        return queryset

class WorkDetailView(DetailView):
	model = Work

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		data = [{
			'user': self.object.user.username,
			'title':self.object.title,
			'category':self.object.category,
			'date':self.object.date,
			'cover':self.object.cover.url,
			'archive':self.object.archive.url,
		}]
		return JsonResponse(data,safe=False)

# Vistas Del API REST

class WorkViewSet(viewsets.ModelViewSet):
	model = Work
	queryset = Work.objects.all()
	serializer_class = WorkSerializer 
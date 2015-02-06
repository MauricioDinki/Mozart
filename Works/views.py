# -*- encoding: utf-8 -*-

from .models import Work
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404,redirect
from django.views.generic import ListView,DetailView,TemplateView
from Thirdauth.mixins import AuthRedirectMixin

class WorkListView(TemplateView):
    template_name = "explore.html"
    model = Work

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

# Vista Para el Home

class HomeView(AuthRedirectMixin,TemplateView):
    template_name = "index.html"

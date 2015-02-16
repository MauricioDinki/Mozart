# -*- encoding: utf-8 -*-

from .forms import UploadWorkForm
from .models import Work
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404,redirect
from django.views.generic import ListView,DetailView,TemplateView,FormView
from Profiles.mixins import RequestFormMixin
from Thirdauth.mixins import AuthRedirectMixin

class HomeView(AuthRedirectMixin,TemplateView):
    template_name = "index.html"

class UploadWorkView(RequestFormMixin,FormView):
	template_name = 'subirobra.html'
	form_class = UploadWorkForm
	success_url =  reverse_lazy('create_work')


	def form_valid(self,form):
		form.save()
		# ctx = {'uploaded':'Obra subia Correctamente','form':form}
		# return render_to_response(self.template_name, ctx, context_instance = RequestContext(self.request))
		return super(UploadWorkView,self).form_valid(form)

class WorkListView(TemplateView):
    template_name = "explore.html"
    model = Work

# class WorkDetailView(DetailView):

# 	model = Work

# 	def get(self, request, *args, **kwargs):
# 		self.object = self.get_object()
# 		data = [{
# 			'user': self.object.user.username,
# 			'title':self.object.title,
# 			'category':self.object.category,
# 			'date':self.object.date,
# 			'cover':self.object.cover.url,
# 			'archive':self.object.archive.url,
# 		}]
# 		return JsonResponse(data,safe=False)




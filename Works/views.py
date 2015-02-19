# -*- encoding: utf-8 -*-

from .forms import UploadWorkForm,EditWorkForm
from .models import Work
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404,redirect
from django.views.generic import ListView,DetailView,TemplateView,FormView,UpdateView
from Profiles.mixins import RequestFormMixin
from Thirdauth.mixins import AuthRedirectMixin, LoginRequiredMixin

class EditWorkView(LoginRequiredMixin,UpdateView):
	template_name = 'edit-work-form.html'
	form_class = EditWorkForm
	success_url =  reverse_lazy('work_list')
	model = Work
	slug_url_kwarg = 'slug'
	slug_field = 'slug'

	def get_object(self):
		obj = self.model.objects.get(user = self.request.user, slug = self.kwargs.get(self.slug_url_kwarg, None))
		return obj

class HomeView(AuthRedirectMixin,TemplateView):
    template_name = "index.html"

class EditWorksView(RequestFormMixin,FormView):
	template_name = 'configuraciones_obras.html'
	form_class = UploadWorkForm
	success_url =  reverse_lazy('edit_works')

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




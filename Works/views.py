# -*- encoding: utf-8 -*-

from .forms import UploadWorkForm,EditWorkForm
from .models import Work
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView,FormView,UpdateView,DeleteView
from Profiles.mixins import RequestFormMixin
from Thirdauth.mixins import AuthRedirectMixin, LoginRequiredMixin

class EditWorkView(LoginRequiredMixin,UpdateView):
	form_class = EditWorkForm
	model = Work
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	success_url =  reverse_lazy('work_list')
	template_name = 'edit-work-form.html'

	def get_object(self):
		obj = get_object_or_404(self.model, user = self.request.user, slug = self.kwargs.get(self.slug_url_kwarg, None))
		return obj

class HomeView(AuthRedirectMixin,TemplateView):
    template_name = "index.html"

class UploadWorkView(RequestFormMixin,FormView):
	form_class = UploadWorkForm
	success_url =  reverse_lazy('create_work')
	template_name = 'subirobra.html'


	def form_valid(self,form):
		form.save()
		# ctx = {'uploaded':'Obra subia Correctamente','form':form}
		# return render_to_response(self.template_name, ctx, context_instance = RequestContext(self.request))
		return super(UploadWorkView,self).form_valid(form)

class WorkListView(TemplateView):
    model = Work
    template_name = "explore.html"

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

@login_required(login_url='login')
def DeleteWorkView(request,slug):
	account_to_delete = get_object_or_404(Work,user = request.user, slug = slug)
	account_to_delete.delete()
	return redirect(reverse_lazy('work_list'))




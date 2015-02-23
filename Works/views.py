# -*- encoding: utf-8 -*-

from .forms import UploadWorkForm,EditWorkForm
from .models import Work
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView,FormView,UpdateView,DeleteView
from Profiles.mixins import RequestFormMixin
from Thirdauth.mixins import AuthRedirectMixin, LoginRequiredMixin


class HomeView(AuthRedirectMixin,TemplateView):
    template_name = "index.html"


class WorkEditView(LoginRequiredMixin,UpdateView):
	form_class = EditWorkForm
	model = Work
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	success_url =  reverse_lazy('settings_works')
	template_name = 'configuraciones_editarobra.html'

	def get_object(self):
		obj = get_object_or_404(self.model, user = self.request.user, slug = self.kwargs.get(self.slug_url_kwarg, None))
		return obj


class WorkListView(TemplateView):
    template_name = "explore.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            if self.kwargs.get('category'):
            	error = get_list_or_404(Work,category = self.kwargs.get('category'))
            	kwargs['category'] = self.kwargs.get('category')
            else:
            	kwargs['category'] = 'all'
    	return kwargs
    	

class WorkSettingsView(TemplateView):
	template_name = 'configuraciones_obras.html'

	def get_context_data(self, **kwargs):
		if 'view' not in kwargs:
		    kwargs['view'] = self
		    kwargs['username'] = self.request.user.username
		return kwargs


class WorkUploadView(RequestFormMixin,FormView):
	form_class = UploadWorkForm
	success_url =  reverse_lazy('work_list')
	template_name = 'subirobra.html'

	def form_valid(self,form):
		form.save()
		# ctx = {'uploaded':'Obra subia Correctamente','form':form}
		# return render_to_response(self.template_name, ctx, context_instance = RequestContext(self.request))
		return super(WorkUploadView,self).form_valid(form)

class WorkUserView(TemplateView):
	template_name = 'perfil_obras.html'

	def get_context_data(self, **kwargs):
		if 'view' not in kwargs:
			kwargs['view'] = self
			kwargs['username'] = self.kwargs.get('username')
			error = get_object_or_404(User,username__iexact = self.kwargs.get('username'))
			if self.kwargs.get('category'):
				error = get_list_or_404(Work,category = self.kwargs.get('category'))
				kwargs['category'] = self.kwargs.get('category')
			else:
				kwargs['category'] = 'all'
			return kwargs


class WorkUserDetailView(TemplateView):
	template_name = 'obra.html'
	def get_context_data(self, **kwargs):
		if 'view' not in kwargs:
		    kwargs['view'] = self
		    kwargs['username'] = self.kwargs.get('username')
		    kwargs['slug'] = self.kwargs.get('slug')
		    error = get_object_or_404(Work,user__username = self.kwargs.get('username'), slug = self.kwargs.get('slug'))
		return kwargs


@login_required(login_url='login')
def WorkDeleteView(request,slug):
	account_to_delete = get_object_or_404(Work,user = request.user, slug = slug)
	account_to_delete.delete()
	return redirect(reverse_lazy('work_list'))
# -*- encoding: utf-8 -*-

from .forms import CreateWorkForm,UpdateWorkForm
from .models import Work
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_list_or_404,redirect,get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, TemplateView, FormView, UpdateView, View
from Profiles.mixins import RequestFormMixin
from Thirdauth.mixins import AuthRedirectMixin, LoginRequiredMixin

class CreateWorkView(LoginRequiredMixin,RequestFormMixin,FormView):
	form_class = CreateWorkForm
	success_url =  reverse_lazy('works:work_list')
	template_name = 'upload_work.html'

	def form_valid(self,form):
		form.save()
		return super(CreateWorkView,self).form_valid(form)

	def get_context_data(self, **kwargs):
	    context = super(CreateWorkView, self).get_context_data(**kwargs)
	    context.update(form=CreateWorkForm())
	    return context

class DetailWorkView(DetailView):
	template_name = 'work.html'
	model = Work
	slug_field = 'slug'
	slug_url_kwarg = 'slug'

class HomeView(AuthRedirectMixin,TemplateView):
    template_name = "welcome_view.html"

class ListWorkView(TemplateView):
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


class SearchProductsView(View):
	template_name = 'search.html'
	work_queryset = Work.objects.all()
	user_queryset = User.objects.all()

	def get(self,request):
		if 'search' in request.GET:
			arg = request.GET['search']
			if arg == '':
				return render_to_response('search_empty.html',context_instance = RequestContext(request))
			works = self.work_queryset.filter(title__icontains = arg)
			users = self.user_queryset.filter(username__icontains = arg)
			ctx = {
				'works':works,
				'users':users,
			}
			return render_to_response(self.template_name,ctx,context_instance = RequestContext(request))
		else:
			return render_to_response('search_empty.html',context_instance = RequestContext(request))


class SettingsWorkView(LoginRequiredMixin,TemplateView):
	template_name = 'settings_works.html'

	def get_context_data(self, **kwargs):
		if 'view' not in kwargs:
		    kwargs['view'] = self
		    kwargs['username'] = self.request.user.username
		return kwargs	

class UpdateWorkView(LoginRequiredMixin,UpdateView):
	form_class = UpdateWorkForm
	model = Work
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	success_url =  reverse_lazy('works:settings_works')
	template_name = 'settings_edit_work.html'

	def get_object(self):
		obj = get_object_or_404(self.model, user = self.request.user, slug = self.kwargs.get(self.slug_url_kwarg, None))
		return obj


class UserWorkView(TemplateView):
	template_name = 'profile_works.html'

	def get_context_data(self, **kwargs):
		if 'view' not in kwargs:
			kwargs['view'] = self
			kwargs['username'] = self.kwargs.get('username')
			if self.kwargs.get('category'):
				kwargs['category'] = self.kwargs.get('category')
			else:
				kwargs['category'] = 'all'
			return kwargs


@login_required(login_url='login')
def DeleteWorkView(request,slug):
	account_to_delete = get_object_or_404(Work,user = request.user, slug = slug)
	account_to_delete.delete()
	return redirect(reverse_lazy('works:work_list'))
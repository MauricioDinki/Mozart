#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from django.core.exceptions import PermissionDenied
from django.http import Http404

from mozart.core.mixins import LoginRequiredMixin, RequestFormMixin
from mozart.core.messages import not_found_messages


from .models import Work
from .forms import WorkCreateForm, WorkUpdateForm


class WorkCreateView(LoginRequiredMixin, RequestFormMixin, CreateView):
    form_class = WorkCreateForm
    success_url = reverse_lazy('works:work_list')
    template_name = 'works/work_create.html'


@login_required(login_url='/')
def WorkDeleteView(request, slug):
    try:
        work_instance = Work.objects.get(user=request.user, slug=slug)
    except Work.DoesNotExist:
        raise PermissionDenied()
    work_instance.delete()
    return redirect(reverse_lazy('works:work_list'))


class WorkDetailView(DetailView):
    model = Work
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'works/work_detail.html'


class WorkListView(TemplateView):
    template_name = 'works/work_list.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            if self.kwargs.get('category'):
                kwarg_category = self.kwargs.get('category')
                category_works = list(Work.objects.filter(category=kwarg_category))
                if not category_works:
                    raise Http404(not_found_messages['404_work_category'])
                kwargs['category'] = self.kwargs.get('category')
            kwargs['category'] = 'all'
        return kwargs


class WorkSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'works/work_settings.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['username'] = self.request.user.username
        return kwargs


class WorkUpdateView(LoginRequiredMixin, UpdateView):
    model = Work
    form_class = WorkUpdateForm
    success_url = reverse_lazy('works:work_settings')
    template_name = 'works/work_update.html'

    def get_object(self):
        try:
            obj = self.model.objects.get(user=self.request.user, slug=self.kwargs.get(self.slug_url_kwarg))
            return obj
        except self.model.DoesNotExist:
            raise PermissionDenied()


class WorkUserView(TemplateView):
    template_name = 'works/work_user_list.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['username'] = self.kwargs.get('username')
            try:
                user = User.objects.get(username__iexact=self.kwargs.get('username'))
                kwargs['user_type'] = user.extendeduser.user_type
            except User.DoesNotExist:
                raise Http404(not_found_messages['404_user'])
            if self.kwargs.get('category'):
                kwarg_category = self.kwargs.get('category')
                category_works = list(Work.objects.filter(category=kwarg_category, user__username__iexact=self.request.user.username))
                if not category_works:
                    raise Http404(not_found_messages['404_work_category'])
                kwargs['category'] = self.kwargs.get('category')
            kwargs['category'] = 'all'
            return kwargs

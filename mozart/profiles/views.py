#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView
from django.http import Http404
from django.core.exceptions import PermissionDenied

from social.apps.django_app.default.models import UserSocialAuth

from mozart.core.mixins import LoginRequiredMixin, RequestFormMixin, SuccessMessage
from mozart.core.messages import success_messages, not_found_messages

from .forms import ChangePasswordForm, ProfileForm


class PasswordUpdateView(SuccessMessage, LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'profiles/password_settings.html'
    form_class = ChangePasswordForm
    success_msg = success_messages['password_update']
    success_url = reverse_lazy('profiles:password_settings')

    def form_valid(self, form):
        form.save()
        return super(PasswordUpdateView, self).form_valid(form)


class ProfileSettingsView(SuccessMessage, LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'profiles/account_settings.html'
    form_class = ProfileForm
    success_msg = success_messages['user_update']
    success_url = reverse_lazy('profiles:account_settings')

    def form_valid(self, form):
        form.save()
        return super(ProfileSettingsView, self).form_valid(form)

    def get_initial(self):
        initial = {
            'address': self.request.user.address.address,
            'city': self.request.user.address.city,
            'description': self.request.user.extendeduser.description,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'nationality': self.request.user.extendeduser.nationality,
            'neighborhood': self.request.user.address.neighborhood,
            'personal_homepage': self.request.user.contact.personal_homepage,
            'profile_picture': self.request.user.extendeduser.profile_picture,
            'phone_number': self.request.user.contact.phone_number,
            'username': self.request.user.username,
            'zip_code': self.request.user.address.zip_code,
        }
        return initial


class ProfileDetailView(TemplateView):
    template_name = 'profiles/profile_detail.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['username'] = self.kwargs.get('username')
            try:
                user = User.objects.get(username__iexact=self.kwargs.get('username'))
            except User.DoesNotExist:
                raise Http404(not_found_messages['404_user'])
            kwargs['user_type'] = user.extendeduser.user_type
            return kwargs


class PromoterListView(TemplateView):
    template_name = "profiles/promoter_list.html"


class SocialNetworkSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/social_settings.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['accounts'] = UserSocialAuth.objects.filter(user__username=self.request.user.username)
        return kwargs


@login_required(login_url=reverse_lazy('xauth:login'))
def SocialNetworkDeleteView(request, provider, account_id):
    try:
        account_instance = UserSocialAuth.objects.get(user__username=request.user.username, provider=provider, id=account_id)
    except UserSocialAuth.DoesNotExist:
        raise PermissionDenied()
    account_instance.delete()
    return redirect(reverse_lazy('profiles:social_settings'))

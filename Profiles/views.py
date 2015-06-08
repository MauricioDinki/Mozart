# -*- encoding:utf-8 -*-

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic import FormView, TemplateView

from social.apps.django_app.default.models import UserSocialAuth

from Profiles.forms import UserInformationForm, ChangePasswordForm
from Utils.mixins import LoginRequiredMixin, RequestFormMixin


class ChangePasswordView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'settings_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('works:index')

    def form_valid(self, form):
        form.save()
        logout(self.request)
        return super(ChangePasswordView, self).form_valid(form)


class ProfileSettingsView(LoginRequiredMixin, RequestFormMixin, FormView):
    template_name = 'settings_information.html'
    form_class = UserInformationForm
    success_url = reverse_lazy('profiles:settings_account')

    def form_valid(self, form):
        form.save()
        ctx = {'updated': 'Perfil Actualizado', 'form': form}
        return render_to_response(self.template_name, ctx, context_instance=RequestContext(self.request))

    def get_initial(self):
        initial = {
            'address': self.request.user.address.address,
            'city': self.request.user.address.city,
            'description': self.request.user.mozart_user.description,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'nationality': self.request.user.mozart_user.nationality,
            'neighborhood': self.request.user.address.neighborhood,
            'personal_homepage': self.request.user.contact.personal_homepage,
            'profile_picture': self.request.user.mozart_user.profile_picture,
            'phone_number': self.request.user.contact.phone_number,
            'username': self.request.user.username,
            'zip_code': self.request.user.address.zip_code,
        }
        return initial


class ProfileView(TemplateView):
    template_name = 'profile_information.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['username'] = self.kwargs.get('username')
            user = get_object_or_404(User, username__iexact=self.kwargs.get('username'))
            kwargs['user_type'] = user.mozart_user.user_type
            return kwargs


class PromoterListView(TemplateView):
    template_name = "promoters-section.html"


class SocialNetworkSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'settings_social.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
            kwargs['cuentas'] = UserSocialAuth.objects.filter(user__username=self.request.user.username)
        return kwargs


@login_required(login_url='login')
def SocialNetworkDeleteView(request, provider, account_id):
    account_to_delete = UserSocialAuth.objects.get(user__username=request.user.username, provider=provider, id=account_id)
    account_to_delete.delete()
    return redirect(reverse_lazy('profiles:settings_social'))

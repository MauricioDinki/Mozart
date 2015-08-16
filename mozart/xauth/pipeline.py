#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from config.settings.base import APPS_DIR

from social.backends.facebook import FacebookOAuth2
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth

from mozart.profiles.models import Facebookauth, Twitterauth, Googleauth


def save_extra_params(request, backend, details, response, uid, user, *args, **kwargs):
    parameters = backend.get_user_details(response)
    social_network_username = parameters['username']
    social_auth_user = kwargs['social']
    new_association = kwargs['new_association']

    if new_association:
        if backend.__class__ is FacebookOAuth2:
            facebookauth_instace = Facebookauth(user=social_auth_user)
            facebookauth_instace.profile_url = response['link']
            facebookauth_instace.network_username = social_network_username
            facebookauth_instace.save()
        elif backend.__class__ is TwitterOAuth:
            twitterauth_instace = Twitterauth(user=social_auth_user)
            twitterauth_instace.profile_url = 'https://twitter.com/%s' % social_network_username
            twitterauth_instace.network_username = social_network_username
            twitterauth_instace.save()
        elif backend.__class__ is GoogleOAuth2:
            googleauth_instance = Googleauth(user=social_auth_user)
            googleauth_instance.profile_url = response['url']
            googleauth_instance.network_username = social_network_username
            googleauth_instance.save()
        return redirect(reverse_lazy('profiles:social_settings'))
    else:
        if backend.__class__ is FacebookOAuth2:
            Plataform = Facebookauth
        elif backend.__class__ is TwitterOAuth:
            Plataform = Twitterauth
            print request
        elif backend.__class__ is GoogleOAuth2:
            Plataform = Googleauth
        try:
            social_network = Plataform.objects.get(user=social_auth_user)
        except Plataform.DoesNotExist:
            return HttpResponse(
                open('%s/templates/http/401_UNSYNCHRONIZED_ACCOUNT.html' % str(APPS_DIR),).read(),
                content_type="text/html",
                status=401
            )
        social_network.network_username = social_network_username
        social_network.save()

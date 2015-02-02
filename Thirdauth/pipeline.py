from social.backends.facebook import FacebookOAuth2
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import ExtendUserSocialAuth
from django.http import Http404

def save_extra_params(backend, details, response, uid, user, *args, **kwargs):
	parameters = backend.get_user_details(response)
	user_username = parameters['username']
	social_user = kwargs['social']
	new_association = kwargs['new_association']
	print new_association

	if new_association:
		extend_name = ExtendUserSocialAuth(user = social_user)

		if backend.__class__ is TwitterOAuth:
			user_username = '@%s'%user_username
			
		extend_name.username_identificator = user_username
		extend_name.save()
	else:
		if backend.__class__ is TwitterOAuth:
			user_username = '@%s'%user_username
		try:
			extend_name = ExtendUserSocialAuth.objects.get(user = social_user )
		except ExtendUserSocialAuth.DoesNotExist:
			raise Http404("No has sincronizado tus cuentas.")
		extend_name.username_identificator = user_username
		extend_name.save()
from social.backends.facebook import FacebookOAuth2
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth
from .models import SocialUserName
from django.contrib.auth.models import User

def save_extra_params(backend, details, response, uid, user, *args, **kwargs):
	parameters = backend.get_user_details(response)
	active_user = User.objects.get(username = kwargs['username'])
	user_username = parameters['username']
	if backend.__class__ is FacebookOAuth2:
		socialusername = SocialUserName.objects.get(user = active_user)
		socialusername.facebook = user_username
		socialusername.save()
	elif backend.__class__ is TwitterOAuth:
		socialusername = SocialUserName.objects.get(user = active_user)
		socialusername.twitter = '@%s'%(user_username)
		socialusername.save()
	elif backend.__class__ is GoogleOAuth2:
		socialusername = SocialUserName.objects.get(user = active_user)
		socialusername.google = user_username
		socialusername.save()


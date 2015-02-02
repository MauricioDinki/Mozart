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
		social_names = SocialUserName(user = active_user)
		social_names.facebook = user_username
		social_names.save()
	# elif backend.__class__ is TwitterOAuth:

	# 	exist_socialusername = SocialUserName.objects.get(user = active_user)
	# 	if exist_socialusername:
	# 		exist_socialusername.twitter = '@%s'%(user_username)
	# 		exist_socialusername.save()
	# 	else:
	# 		social_names = SocialUserName(user = active_user)
	# 		social_names.twitter = '@%s'%(user_username)
	# 		social_names.save()

	# elif backend.__class__ is GoogleOAuth2:

	# 	exist_socialusername = SocialUserName.objects.get(user = active_user)
	# 	if exist_socialusername:
	# 		exist_socialusername.google = user_username
	# 		exist_socialusername.save()
	# 	else:
	# 		social_names = SocialUserName(user = active_user)
	# 		social_names.google = user_username
	# 		social_names.save()


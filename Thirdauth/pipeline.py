from .models import ExtendUserSocialAuth
from django.http import Http404,HttpResponseRedirect
from Profiles.models import Social_Network_Facebook_URL,Social_Network_Twitter_URL,Social_Network_Google_URL
from social.backends.facebook import FacebookOAuth2
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth


def save_extra_params(backend, details, response, uid, user, *args, **kwargs):
	parameters = backend.get_user_details(response)
	user_username = parameters['username']
	social_user = kwargs['social']
	new_association = kwargs['new_association']

	if new_association:
		extend_name = ExtendUserSocialAuth(user = social_user)			
		extend_name.username_identificator = user_username
		extend_name.save()

		if backend.__class__ is FacebookOAuth2:
			facebook_profile_url = response['link']
			instancia_facebook_url = Social_Network_Facebook_URL(user = social_user)
			instancia_facebook_url.facebook = facebook_profile_url
			instancia_facebook_url.save()
		elif backend.__class__ is TwitterOAuth:
			twitter_profile_url = 'https://twitter.com/%s'%(response['screen_name'])
			instancia_twitter_url = Social_Network_Twitter_URL(user = social_user)
			instancia_twitter_url.twitter = twitter_profile_url
			instancia_twitter_url.save()
		elif backend.__class__ is GoogleOAuth2:
			google_profile_url = response['url']
			instancia_google_url = Social_Network_Google_URL(user = social_user)
			instancia_google_url.google = google_profile_url
			instancia_google_url.save()

		return HttpResponseRedirect('/configuracion/cuentas')
	else:
		try:
			extend_name = ExtendUserSocialAuth.objects.get(user = social_user )
		except ExtendUserSocialAuth.DoesNotExist:
			raise Http404("No has sincronizado tus cuentas.")
		extend_name.username_identificator = user_username
		extend_name.save()


	# if backend.__class__ is FacebookOAuth2:
	# 	facebook_profile_url = response['link']
	# 	facebook_url_model = Social_Network_Facebook_URL.objects.get(user = social_user)
	# 	facebook_url_model.facebook = facebook_profile_url
	# 	facebook_url_model.save()
	# elif backend.__class__ is GoogleOAuth2:
	# 	google_profile_url = response['url']
	# 	google_url_model = Social_Network_Google_URL.objects.get(user = social_user)
	# 	google_url_model.google = google_profile_url
	# 	google_url_model.save()
	# elif backend.__class__ is TwitterOAuth:
	# 	twitter_profile_url = 'https://twitter.com/%s'%(response['screen_name'])
	# 	twitter_url_model = Social_Network_Twitter_URL.objects.get(user = social_user)
	# 	twitter_url_model.twitter = twitter_profile_url
	# 	twitter_url_model.save()

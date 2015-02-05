from .models import ExtendUserSocialAuth
from django.http import Http404,HttpResponseRedirect
from Profiles.models import Social_Network_URL
from social.backends.facebook import FacebookOAuth2
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth
from social.backends.twitter import TwitterOAuth

def save_extra_params(backend, details, response, uid, user, *args, **kwargs):
	parameters = backend.get_user_details(response)
	user_username = parameters['username']
	social_user = kwargs['social']
	print social_user
	new_association = kwargs['new_association']

	if new_association:
		extend_name = ExtendUserSocialAuth(user = social_user)			
		extend_name.username_identificator = user_username
		extend_name.save()
		return HttpResponseRedirect('/configuracion/cuentas')
	else:
		try:
			extend_name = ExtendUserSocialAuth.objects.get(user = social_user )
		except ExtendUserSocialAuth.DoesNotExist:
			raise Http404("No has sincronizado tus cuentas.")
		extend_name.username_identificator = user_username
		extend_name.save()


	# if backend.__class__ is FacebookOAuth2:
	# 	print 'Iniciaste con facebook'
	# elif backend.__class__ is GoogleOAuth2:
	# 	print 'Iniciaste con google'
	# elif backend.__class__ is TwitterOAuth:
	# 	print 'Iniciaste con twitter'
	# print response

	# para facebook
	# url_perfil = response['link']
	# print url_perfil

	# para google
	# url_perfil = response['url'] 
	# print url_perfil

	# para twitter
	# url_perfil = 'https://twitter.com/%s'%(response['screen_name'])
	# print url_perfil
from social.backends.facebook import FacebookOAuth2
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth

def save_extra_params(backend, details, response, uid, user, *args, **kwargs):
	parameters = backend.get_user_details(response)
	user_username = parameters['username']
	if backend.__class__ is FacebookOAuth2:
		print 'Iniciaste con facebook'
	elif backend.__class__ is GoogleOAuth2:
		print 'Iniciaste con google'
	elif backend.__class__ is TwitterOAuth:
		print 'Iniciaste con twitter'

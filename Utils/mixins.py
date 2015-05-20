# -*- encoding: utf-8 -*-

from rest_framework import serializers

class RequestFormMixin(object):
	'''
		This mixin put the request in the form kwargs to be used in the form
	'''
	def get_form_kwargs(self):
		kwargs = super( RequestFormMixin,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

class UsernameSerializerMixin(object):
	'''
		This mixin show the username for a user in the api instead of the user url
	'''
	user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
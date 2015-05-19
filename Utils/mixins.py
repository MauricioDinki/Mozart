# -*- encoding: utf-8 -*-

class RequestFormMixin(object):
	'''
		This mixin put the request in the form kwargs to be used in the form
	'''
	def get_form_kwargs(self):
		kwargs = super( RequestFormMixin,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs
# -*- encoding: utf-8 -*-

class RequestFormMixin(object):
	def get_form_kwargs(self):
		kwargs = super( RequestFormMixin,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

# -*- encoding: utf-8 -*-

class RequestFormMixin(object):
	def get_form_kwargs(self):
		kwargs = super( RequestFormMixin,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs


class FilterUsernameMixin(object):
	def get_queryset(self):
		username = self.request.query_params.get('username', None)
		paginate = self.request.query_params.get('paginate')
		if username is not None:
			queryset = self.queryset.filter(user__username = username)[:paginate]
		else:
			queryset = self.queryset
		return queryset

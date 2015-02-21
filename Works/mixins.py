class WorkListUserMixin(object):
	def get_context_data(self, **kwargs):
		if 'view' not in kwargs:
		    kwargs['view'] = self
		    kwargs['username'] = self.request.user.username
		return kwargs
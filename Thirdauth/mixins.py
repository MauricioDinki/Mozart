# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

class AuthRedirectMixin(object):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('work_list')
		else:
		    return super(AuthRedirectMixin, self).get(self, request, *args, **kwargs)

class LoginRequiredMixin(object):
	@method_decorator(login_required(login_url='login'))
	def dispatch(self, request, *args, **kwargs):
	    return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

# class LoginRequiredMixinUpdate(object):
# 	@method_decorator(login_required(login_url='login'))
# 	def dispatch(self, request, *args, **kwargs):
# 	    if request.method.lower() in self.http_method_names:
# 	        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
# 	    else:
# 	        handler = self.http_method_not_allowed
# 	    return handler(request, *args, **kwargs)
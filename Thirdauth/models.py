# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from social.apps.django_app.default.models import UserSocialAuth

class ExtendUserSocialAuth(models.Model):
	user = models.OneToOneField(UserSocialAuth)
	username_identificator = models.CharField(blank=True,null=True, max_length=50)

	def __unicode__(self):
		return self.user.user.username

	class Meta:
		verbose_name = "Usernames for social networks"
		verbose_name_plural = "Usernames for social networks"
    

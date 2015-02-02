# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class SocialUserName(models.Model):
	user = models.OneToOneField(User)
	facebook = models.CharField(blank=True,null=True, max_length=50)
	twitter = models.CharField(blank=True,null=True, max_length=50)
	google = models.CharField(blank=True,null=True, max_length=50)

	class Meta:
		verbose_name = "Social username"
		verbose_name_plural = "Social username"

	def __unicode__(self):
		return self.user.username


# -*- encoding: utf-8 -*-

from django.db import models

class SocialUserName(models.Model):
	facebook = models.CharField(required=False,null=False, max_length=50)
	twitter = models.CharField(required=False,null=False, max_length=50)
	google = models.CharField(required=False,null=False, max_length=50)
    class Meta:
        verbose_name = "Social username"
        verbose_name_plural = "Social username"

    def __str__(self):
        pass


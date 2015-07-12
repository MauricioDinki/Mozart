#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from social.apps.django_app.default.models import UserSocialAuth


class ExtendUserSocialAuth(models.Model):
    user = models.OneToOneField(
        UserSocialAuth,
        verbose_name=_('Social auth user'),
    )
    network_username = models.CharField(
        _('Social Network Username'),
        blank=True,
        null=True,
        max_length=50,
    )

    class Meta:
        verbose_name = _('Social network username')
        verbose_name_plural = _('Social network usernames')

    def __unicode__(self):
        return self.user.user.username

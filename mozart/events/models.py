#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


def event_cover_url(self, filename):
    return str('event-cover/%s/%s') % (self.user.username, filename)


class Event(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        null=False,
    )
    cover = models.ImageField(
        _('Cover'),
        blank=False,
        null=False,
        upload_to=event_cover_url
    )
    date = models.DateField(
        _('Date'),
        blank=False,
        null=False,
    )
    description = models.CharField(
        _('Description'),
        blank=False,
        max_length=1000,
        null=False,
    )
    finish_time = models.TimeField(
        _('Finish time'),
        blank=False,
        null=False,
    )
    name = models.CharField(
        _('Name'),
        blank=False,
        max_length=50,
        null=False,
        unique=True,
    )
    place = models.CharField(
        _('Place'),
        blank=False,
        max_length=200,
        null=False,
    )
    slug = models.SlugField(
        _('Slug'),
        max_length=50,
        unique=True,
    )
    start_time = models.TimeField(
        _('Start time'),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __unicode__(self):
        return self.name

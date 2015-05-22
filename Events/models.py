# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


def event_cover_url(self, filename):
    return str('event-cover/%s/%s') % (self.user.username, filename)


class Event(models.Model):
    cover = models.FileField(
        blank=True,
        null=True,
        upload_to=event_cover_url
    )
    date = models.DateField(
        blank=True,
        null=True,
    )
    description = models.CharField(
        blank=True,
        max_length=200,
        null=True,
    )
    finish_time = models.TimeField(
        blank=True,
        null=True,
    )
    name = models.CharField(
        blank=True,
        max_length=50,
        null=True,

    )
    place = models.CharField(
        blank=True,
        max_length=50,
        null=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    start_time = models.TimeField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        null=True,
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __unicode__(self):
        return self.name

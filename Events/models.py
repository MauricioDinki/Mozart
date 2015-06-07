# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


def event_cover_url(self, filename):
    return str('event-cover/%s/%s') % (self.user.username, filename)


class Event(models.Model):

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    cover = models.ImageField(
        blank=False,
        null=False,
        upload_to=event_cover_url
    )
    date = models.DateField(
        blank=False,
        null=False,
    )
    description = models.CharField(
        blank=False,
        max_length=1000,
        null=False,
    )
    finish_time = models.TimeField(
        blank=False,
        null=False,
    )
    name = models.CharField(
        blank=False,
        max_length=50,
        null=False,
    )
    place = models.CharField(
        blank=False,
        max_length=200,
        null=False,
    )
    slug = models.SlugField(
        max_length=50,
        unique=False,
    )
    start_time = models.TimeField(
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        User,
        null=False,
    )

    def __unicode__(self):
        return self.name

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


def archive_url(self, filename):
    return str('files/%s/%s') % (self.user.username, filename)


def cover_url(self, filename):
    return str('covers/%s/%s') % (self.user.username, filename)


CATEGORY = (
    ('drawing-painting', _('Drawing / Painting')),
    ('photography-film', _('Photography / Film ')),
    ('theater-literature', _('Theater / Literature ')),
    ('music-dance', _('Music / Dance')),
    ('sculpture-ceramics', _('Sculpture / Ceramics ')),
    ('digital_art', _('Digital Art')),
    ('other', _('Other')),
)

FILES = (
    ('image', _('Image')),
    ('audio', _('Audio')),
)


class Work(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(
        _('Title'),
        blank=False,
        max_length=50,
        null=False,
        unique=True,
    )
    description = models.CharField(
        _('Description'),
        blank=False,
        max_length=200,
        null=False,
    )
    category = models.CharField(
        _('Category'),
        blank=False,
        choices=CATEGORY,
        max_length=50,
        null=False,
    )
    date = models.DateTimeField(
        _('Creation date'),
        auto_now_add=True,
        blank=False,
        null=False,
    )
    cover = models.ImageField(
        _('Work cover'),
        blank=False,
        null=False,
        upload_to=cover_url,
    )
    archive = models.FileField(
        _('Work file'),
        blank=False,
        null=False,
        upload_to=archive_url,
    )
    slug = models.SlugField(
        _('Slug'),
        max_length=50,
        unique=True,
    )
    work_type = models.CharField(
        _('Work type'),
        blank=False,
        choices=FILES,
        max_length=50,
        null=False,
    )

    class Meta:
        verbose_name = _('Work')
        verbose_name_plural = _('Works')

    def __unicode__(self):
        return self.title

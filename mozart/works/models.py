#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


def archive_url(self, filename):
    return str('files/%s/%s') % (self.user.username, filename)


def cover_url(self, filename):
    return str('covers/%s/%s') % (self.user.username, filename)


CATEGORY = (
    ('dibujo-pintura', 'Dibujo/Pintura'),
    ('fotografia-filme', 'Fotografia/Filme'),
    ('teatro-literatura', 'Teatro/Literatura'),
    ('musica-baile', 'Musica/Baile'),
    ('escultura-ceramica', 'Escultura/Ceramica'),
    ('arte_digital', 'Arte digital'),
    ('otros', 'Otros'),
)

FILES = (
    ('image', 'Imagen'),
    ('audio', 'Audio'),
)


class Work(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(
        blank=False,
        max_length=50,
        null=False,
        unique=True,
    )
    description = models.CharField(
        blank=False,
        max_length=200,
        null=False,
    )
    category = models.CharField(
        blank=False,
        choices=CATEGORY,
        max_length=50,
        null=False,
    )
    date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    cover = models.ImageField(
        blank=False,
        null=False,
        upload_to=cover_url,
    )
    archive = models.FileField(
        blank=False,
        null=False,
        upload_to=archive_url,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    work_type = models.CharField(
        blank=False,
        choices=FILES,
        max_length=50,
        null=False,
    )

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("works:detail", kwargs={"slug": self.slug})

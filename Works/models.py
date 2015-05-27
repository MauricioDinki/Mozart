# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from sorl.thumbnail import ImageField


def archive_url(self, filename):
    return str('files/%s/%s') % (self.user.username, filename)


def cover_url(self, filename):
    return str('covers/%s/%s') % (self.user.username, filename)


def thumbnail_url(self, filename):
    return str('thumbnails/%s/%s') % (self.user.username, filename)


category = (
    ('', ''),
    ('dibujo-pintura', 'Dibujo/Pintura'),
    ('fotografia-filme', 'Fotografia/Filme'),
    ('teatro-literatura', 'Teatro/Literatura'),
    ('musica-baile', 'Musica/Baile'),
    ('escultura-ceramica', 'Escultura/Ceramica'),
    ('arte_digital', 'Arte digital'),
    ('otros', 'Otros'),
)

files = (
    ('', ''),
    ('image', 'Imagen'),
    ('audio', 'Audio'),
)


class Work(models.Model):

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

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
        choices=category,
        max_length=50,
        null=False,
    )
    date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    cover = ImageField(
        blank=False,
        null=False,
        upload_to=cover_url,
    )
    thumbnail = ImageField(
        blank=True,
        null=True,
        upload_to=thumbnail_url,
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
        choices=files,
        max_length=50,
        null=False,
    )

    def __unicode__(self):
        return self.title

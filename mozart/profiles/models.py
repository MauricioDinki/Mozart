#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField
from social.apps.django_app.default.models import UserSocialAuth

from mozart.core.messages import DAYS, MONTHS, SEXUALITY, USER_TYPE


def profile_picture_url(self, filename):
    return str('profile-images/%s/%s') % (self.user.username, filename)


def presentation_file_url(self, filename):
    return str('presentation-file/%s/%s') % (self.user.username, filename)


class Address(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_('User')
    )
    address = models.CharField(
        _('Address'),
        blank=True,
        max_length=50,
        null=True,
    )
    city = models.CharField(
        _('City'),
        blank=True,
        max_length=50,
        null=True,
    )
    zip_code = models.CharField(
        _('Zip code'),
        blank=True,
        max_length=10,
        null=True,
    )
    neighborhood = models.CharField(
        _('Neighborhood'),
        blank=True,
        max_length=50,
        null=True,
    )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __unicode__(self):
        return self.user.username


class Birthday(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_('User')
    )
    day = models.CharField(
        _('Day'),
        blank=True,
        choices=DAYS,
        max_length=50,
        null=True,
    )
    month = models.CharField(
        _('Month'),
        blank=True,
        choices=MONTHS,
        max_length=50,
        null=True,
    )
    year = models.IntegerField(
        _('Year'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Birthday')
        verbose_name_plural = _('Birthdays')

    def __unicode__(self):
        return self.user.username


class Contact(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='User',
    )
    personal_homepage = models.URLField(
        _('Personal homepage'),
        blank=True,
        max_length=50,
        null=True,
    )
    phone_number = models.BigIntegerField(
        _('Phone number'),
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class ExtendedUser(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_('User'),
    )
    description = models.CharField(
        _('Description'),
        blank=True,
        max_length=200,
        null=True,
    )
    nationality = CountryField(
        _('Nationality'),
        blank=True,
        max_length=200,
        null=True,
    )
    presentation_file = models.FileField(
        _('Presentation file'),
        blank=True,
        null=True,
        upload_to=presentation_file_url,
    )
    profile_picture = models.ImageField(
        _('Profile picture'),
        blank=True,
        null=True,
        upload_to=profile_picture_url
    )
    sex = models.CharField(
        _('Sex'),
        blank=True,
        choices=SEXUALITY,
        max_length=50,
        null=True,
    )
    user_type = models.CharField(
        _('User type'),
        blank=True,
        choices=USER_TYPE,
        max_length=50,
        null=True,
    )

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Mozart user')
        verbose_name_plural = _('Mozart users')

    def get_nationality(self):
        return self.nationality.name


class Facebookauth(models.Model):
    user = models.OneToOneField(
        UserSocialAuth,
        verbose_name=_('User'),
    )
    profile_url = models.URLField(
        _('Facebook profile url'),
        blank=True,
        max_length=200,
        null=True,
    )

    network_username = models.CharField(
        _('Social Network Username'),
        blank=True,
        null=True,
        max_length=50,
    )

    class Meta:
        verbose_name = _("Facebook information")
        verbose_name_plural = _("Facebook information")

    def __unicode__(self):
        return self.user.user.username


class Googleauth(models.Model):
    user = models.OneToOneField(
        UserSocialAuth,
        verbose_name=_('User'),
    )
    profile_url = models.URLField(
        _('Google profile url'),
        blank=True,
        max_length=200,
        null=True,
    )

    network_username = models.CharField(
        _('Social Network Username'),
        blank=True,
        null=True,
        max_length=50,
    )

    class Meta:
        verbose_name = _("Google information")
        verbose_name_plural = _("Google information")

    def __unicode__(self):
        return self.user.user.username


class Twitterauth(models.Model):
    user = models.OneToOneField(
        UserSocialAuth,
        verbose_name=_('User'),
    )
    profile_url = models.URLField(
        _('Twitter profile url'),
        blank=True,
        max_length=200,
        null=True,
    )

    network_username = models.CharField(
        _('Social Network Username'),
        blank=True,
        null=True,
        max_length=50,
    )

    class Meta:
        verbose_name = _("Twitter information")
        verbose_name_plural = _("Twitter information")

    def __unicode__(self):
        return self.user.user.username

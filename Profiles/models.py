# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from django_countries.fields import CountryField
from social.apps.django_app.default.models import UserSocialAuth
from sorl.thumbnail import ImageField

days = (
    ('', 'Dia'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

months = (
    ('', 'Mes'),
    ('Enero', 'Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre'),
)

sexuality = (
    ('', 'Sexo'),
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)

type_of_users = (
    ('', 'Seleccionar tipo de cuenta'),
    ('Artista', 'Artista'),
    ('Promotor', 'Promotor'),
)


def profile_picture_url(self, filename):
    return str('profile-images/%s/%s') % (self.user.username, filename)


def presentation_file_url(self, filename):
    return str('presentation-file/%s/%s') % (self.user.username, filename)


class Mozart_User(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(
        blank=True,
        max_length=200,
        null=True,
    )
    nationality = CountryField(
        blank=True,
        max_length=200,
        null=True,
    )
    presentation_file = models.FileField(
        blank=True,
        null=True,
        upload_to=presentation_file_url,
    )
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to=profile_picture_url
    )
    thumbnail = ImageField(
        blank=True,
        null=True,
        upload_to='null',
    )
    sex = models.CharField(
        blank=True,
        choices=sexuality,
        max_length=50,
        null=True,
    )
    user_type = models.CharField(
        blank=True,
        choices=type_of_users,
        max_length=50,
        null=True,
    )

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = "Mozart User"
        verbose_name_plural = "Mozart Users"

    def get_nationality(self):
        return self.nationality.name


class Contact(models.Model):
    user = models.OneToOneField(User)
    personal_homepage = models.URLField(
        blank=True,
        max_length=50,
        null=True,
    )
    phone_number = models.BigIntegerField(
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Facebook_URL(models.Model):
    user = models.OneToOneField(UserSocialAuth)
    facebook = models.URLField(
        blank=True,
        max_length=200,
        null=True,
    )

    class Meta:
        verbose_name = "Facebook Profile URL"
        verbose_name_plural = "Facebook Profile URL"

    def __unicode__(self):
        return self.user.user.username


class Twitter_URL(models.Model):
    user = models.OneToOneField(UserSocialAuth)
    twitter = models.URLField(
        blank=True,
        max_length=200,
        null=True,
    )

    class Meta:
        verbose_name = "Twitter Profile URL"
        verbose_name_plural = "Twitter Profile URL"

    def __unicode__(self):
        return self.user.user.username


class Google_URL(models.Model):
    user = models.OneToOneField(UserSocialAuth)
    google = models.URLField(
        blank=True,
        max_length=200,
        null=True,
    )

    class Meta:
        verbose_name = "Google Profile URL"
        verbose_name_plural = "Google Profile URL"

    def __unicode__(self):
        return self.user.user.username


class Date_of_Birth(models.Model):
    user = models.OneToOneField(User)
    day = models.CharField(
        blank=True,
        choices=days,
        max_length=50,
        null=True,
    )
    month = models.CharField(
        blank=True,
        choices=months,
        max_length=50,
        null=True,
    )
    year = models.IntegerField(
        blank=True,
        max_length=4,
        null=True,
    )

    class Meta:
        verbose_name = "Date of Birth"
        verbose_name_plural = "Date of Birth"

    def __unicode__(self):
        return self.user.username


class Address(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(
        blank=True,
        max_length=50,
        null=True,
    )
    city = models.CharField(
        blank=True,
        max_length=50,
        null=True,
    )
    zip_code = models.CharField(
        blank=True,
        max_length=10,
        null=True,
    )
    neighborhood = models.CharField(
        blank=True,
        max_length=50,
        null=True,
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address"

    def __unicode__(self):
        return self.user.username

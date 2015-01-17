# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from sorl.thumbnail import ImageField

sexuality = (
	('Masculino', 'Masculino'),
	('Femenino', 'Femenino'),)

days = (
	('',''),
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
	('9','9'),
	('10','10'),
	('11','11'),
	('12','12'),
	('13','13'),
	('14','14'),
	('15','15'),
	('16','16'),
	('17','17'),
	('18','18'),
	('19','19'),
	('20','20'),
	('21','21'),
	('22','22'),
	('23','23'),
	('24','24'),
	('25','25'),
	('26','26'),
	('27','27'),
	('28','28'),
	('29','29'),
	('30','30'),
	('31','31'),)

months = (
	('',''),
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
	('Diciembre', 'Diciembre'),)


def profile_picture_url(self,filename):
	return str('profile-images/%s/%s')%(self.user.username,filename)

def presentation_file_url(self,filename):
	return str('presentation-file/%s/%s')%(self.user.username,filename)
	
class Mozart_User(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(blank=True,null=True, max_length=200)
	nationality = CountryField(blank=True,null=True)
	presentation_file = models.FileField(blank=True,null=True,upload_to=presentation_file_url)
	profile_picture = ImageField(blank=True,null=True,upload_to=profile_picture_url)
	sex = models.CharField(blank=True,null=True, max_length=50,choices=sexuality)
	user_type = models.CharField(blank=True,null=True, max_length=50)

	def __unicode__(self):
		return self.user.username

	class Meta:
		verbose_name = "Mozart User"
		verbose_name_plural = "Mozart Users"

	
class Contact(models.Model):
	user = models.OneToOneField(User)
	personal_homepage = models.URLField(blank=True,null=True, max_length=50)
	phone_number = models.BigIntegerField(blank=True,null=True)

	def __unicode__(self):
		return self.user.username

	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contact'


class Social_Network(models.Model):
	user = models.OneToOneField(User)
	facebook = models.URLField(blank=True,null=True, max_length=50)
	google = models.URLField(blank=True,null=True, max_length=50)
	twitter = models.URLField(blank=True,null=True, max_length=50)
	youtube = models.URLField(blank=True,null=True, max_length=50)

	class Meta:
		verbose_name = "Social Network"
		verbose_name_plural = "Social Networks"

	def __unicode__(self):
		return self.user.username

class Date_of_Birth(models.Model):
	user = models.OneToOneField(User)
	day = models.CharField(blank=True,null=True, max_length=50,choices=days)
	month = models.CharField(blank=True,null=True, max_length=50,choices=months)
	year = models.IntegerField(blank=True,null=True,max_length=4)

	class Meta:
		verbose_name = "Date of Birth"
		verbose_name_plural = "Date of Birth"

	def __unicode__(self):
		return self.user.username
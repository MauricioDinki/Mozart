# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from sorl.thumbnail import ImageField

sexuality = (
	('Masculino', 'Masculino'),
	('Femenino', 'Femenino'),
)

def profile_picture_url(self,filename):
	return str('profile-images/%s/%s')%(self.user.username,filename)

def presentation_file_url(self,filename):
	return str('presentation-file/%s/%s')%(self.user.username,filename)
	pass
	
class Artist(models.Model):
	user = models.OneToOneField(User)
	date_of_birth = models.DateField(blank=True,null=True)
	sex = models.CharField(blank=True,null=True, max_length=50,choices=sexuality)
	nationality = CountryField(blank=True,null=True)
	profile_picture = ImageField(blank=True,null=True,upload_to=profile_picture_url)
	presentation_file = models.FileField(blank=True,null=True,upload_to=presentation_file_url)

	class Meta:
		verbose_name = "Artist"
		verbose_name_plural = "Artists"

	def __unicode__(self):
		return self.user.username
	
class Contact(models.Model):
	user = models.OneToOneField(User)
	phone_number = models.BigIntegerField(blank=True,null=True)
	adress = models.CharField(blank=True,null=True, max_length=50)

	def __unicode__(self):
		return self.user.username

class SocialNetwork(models.Model):
	user = models.OneToOneField(User)
	facebook = models.URLField(blank=True,null=True, max_length=50)
	twitter = models.URLField(blank=True,null=True, max_length=50)
	youtube = models.URLField(blank=True,null=True, max_length=50)
	google = models.URLField(blank=True,null=True, max_length=50)

	class Meta:
		verbose_name = "Social Network"
		verbose_name_plural = "Social Networks"

	def __unicode__(self):
		return self.user.username
    
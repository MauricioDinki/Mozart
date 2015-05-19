from django.db import models
from Profiles.models import days,months
from django.utils.text import slugify
from django.contrib.auth.models import User

def event_cover_url(self,filename):
	return str('event-cover/%s/%s')%(self.user.username,filename)

class Event(models.Model):
	"""
		DB model for events
	"""
	user = models.ForeignKey(
		User,
		null=True,
	)
	name = models.CharField(
		blank=True,
		max_length=50,
		null=True,
	)
	description = models.CharField(
		blank=True,
		max_length=200,
		null=True,
	)
	cover = models.FileField(
		blank=True,
		null=True,
		upload_to=event_cover_url
	)
	date = models.DateField(
		blank=True,
		null=True,
	)

	start_time = models.TimeField(
		blank=True,
		null=True,
	)
	finish_time = models.TimeField(
		blank=True,
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

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

	def __unicode__(self):
		return self.name
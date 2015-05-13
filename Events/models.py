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
	user = models.OneToOneField(
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
	day = models.CharField(
		blank=True,
		max_length=50,
		null=True, 
		choices=days
	)
	month = models.CharField(
		blank=True,
		max_length=50,
		null=True, 
		choices=months
	)
	year = models.IntegerField(
		blank=True,
		max_length=4,
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
		blank=True,
		max_length=50,
		null=True,
		unique=True,

	)

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Event, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name
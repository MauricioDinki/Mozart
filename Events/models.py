from django.db import models
from Profiles.models import days,months
from django.utils.text import slugify

def event_cover_url(self,filename):
	return str('event-cover/%s/%s')%(self.user.username,filename)

class Event(models.Model):
	name = models.CharField(
		blank=True,
		null=True,
		max_length=50,
	)
	description = models.CharField(
		blank=True,
		null=True,
		max_length=200
	)
	cover = models.FileField(
		blank=True,
		null=True,
		upload_to=event_cover_url
	)
	day = models.CharField(
		blank=True,
		null=True, 
		max_length=50,
		choices=days
	)
	month = models.CharField(
		blank=True,
		null=True, 
		max_length=50,
		choices=months
	)
	year = models.IntegerField(
		blank=True,
		null=True,
		max_length=4
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
		null=True,
		max_length=50
	)
	slug = models.SlugField(
		max_length=50,
		unique=True,
	)

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Work, self).save(*args, **kwargs)
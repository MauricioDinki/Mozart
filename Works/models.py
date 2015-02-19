# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField

def archive_url(self,filename):
	return str('files/%s/%s')%(self.user.username,filename)

def cover_url(self,filename):
	return str('covers/%s/%s')%(self.user.username,filename)

category = (
	('','Selecciona la categoría'),
	('dibujo-pintura','Dibujo/Pintura'),
	('fotografia-filme','Fotografia/Filme'),
	('teatro-literatura','Teatro/Literatura'),
	('musica-baile','Musica/Baile'),
	('escultura-ceramica','Escultura/Ceramica'),
	('arte_digital','Arte digital'),
	('otros','Otros'),
)

class Work(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(blank=False,null=False, max_length=50,unique=True)
	description = models.CharField(blank=False,null=False, max_length=200)
	category = models.CharField(blank=False,null=False, max_length=50,choices=category)
	date = models.DateField(blank=False,null=False,auto_now_add=True)
	cover = ImageField(null=False,blank=False,upload_to=cover_url)
	archive = models.FileField(blank=False,null=False,upload_to=archive_url)
	slug = models.SlugField(max_length=50,unique=True)

	class Meta:
		verbose_name = "Work"
		verbose_name_plural = "Works"

	def __unicode__(self):
		return self.title

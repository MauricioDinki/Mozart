# -*- encoding: utf-8 -*-
from .models import Artist
from django.contrib import admin

@admin.register(Artist)
class AdminArtist(admin.ModelAdmin):
	pass

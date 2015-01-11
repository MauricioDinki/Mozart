# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Artist,Contact,SocialNetwork

@admin.register(Artist)
class AdminArtist(admin.ModelAdmin):
	pass

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
	pass

@admin.register(SocialNetwork)
class AdminSocialNetwork(admin.ModelAdmin):
	pass


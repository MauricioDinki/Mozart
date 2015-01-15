# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Mozart_User,Contact,Social_Network,Date_of_Birth

@admin.register(Mozart_User)
class AdminMozartUser(admin.ModelAdmin):
	pass

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
	pass

@admin.register(Social_Network)
class AdminSocialNetwork(admin.ModelAdmin):
	pass

@admin.register(Date_of_Birth)
class AdminDateBirth(admin.ModelAdmin):
	pass


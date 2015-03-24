# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Mozart_User,Contact,Date_of_Birth,Social_Network_Facebook_URL,Social_Network_Twitter_URL,Social_Network_Google_URL,Adress

@admin.register(Mozart_User)
class AdminMozartUser(admin.ModelAdmin):
	list_display = ('user','sex','nationality', 'user_type',)
	list_filter = ('user','sex','nationality', 'user_type',)

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
	list_display = ('user','personal_homepage','phone_number',)
	list_filter = ('user','personal_homepage','phone_number',)

@admin.register(Date_of_Birth)
class AdminDateBirth(admin.ModelAdmin):
	list_display = ('user','day','month','year',)
	list_filter = ('user','day','month','year',)

@admin.register(Social_Network_Facebook_URL)
class AdminFacebookURL(admin.ModelAdmin):
	list_display = ('user','facebook',)

@admin.register(Social_Network_Twitter_URL)
class AdminTwitterURL(admin.ModelAdmin):
	list_display = ('user','twitter',)

@admin.register(Social_Network_Google_URL)
class AdminGoolgeURL(admin.ModelAdmin):
	list_display = ('user','google',)

@admin.register(Adress)
class AdminAdress(admin.ModelAdmin):
	list_display = ('user','adress','city','zip_code','neighborhood')


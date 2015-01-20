# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Mozart_User,Contact,Social_Network,Date_of_Birth

@admin.register(Mozart_User)
class AdminMozartUser(admin.ModelAdmin):
	list_display = ('sex','nationality', 'user_type',)
	list_filter = ('sex','nationality', 'user_type',)

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
	list_display = ('user','personal_homepage','phone_number',)
	list_filter = ('user','personal_homepage','phone_number',)


@admin.register(Social_Network)
class AdminSocialNetwork(admin.ModelAdmin):
	list_display = ('user','facebook','twitter','google','youtube')
	list_filter = ('user','facebook','twitter','google','youtube')

@admin.register(Date_of_Birth)
class AdminDateBirth(admin.ModelAdmin):
	list_display = ('user','day','month','year',)
	list_filter = ('user','day','month','year',)


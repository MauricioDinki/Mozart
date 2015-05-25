# -*- encoding: utf-8 -*-

from django.contrib import admin
from Profiles.models import Mozart_User, Contact, Date_of_Birth, Facebook_URL, Twitter_URL, Google_URL, Address


@admin.register(Mozart_User)
class AdminMozartUser(admin.ModelAdmin):
    list_display = ('user', 'sex', 'nationality', 'user_type',)
    list_filter = ('user', 'sex', 'nationality', 'user_type',)


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('user', 'personal_homepage', 'phone_number',)
    list_filter = ('user', 'personal_homepage', 'phone_number',)


@admin.register(Date_of_Birth)
class AdminDateBirth(admin.ModelAdmin):
    list_display = ('user', 'day', 'month', 'year',)
    list_filter = ('user', 'day', 'month', 'year',)


@admin.register(Facebook_URL)
class AdminFacebookURL(admin.ModelAdmin):
    list_display = ('user', 'facebook',)


@admin.register(Twitter_URL)
class AdminTwitterURL(admin.ModelAdmin):
    list_display = ('user', 'twitter',)


@admin.register(Google_URL)
class AdminGoolgeURL(admin.ModelAdmin):
    list_display = ('user', 'google',)


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'zip_code', 'neighborhood')

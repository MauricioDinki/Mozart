#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'zip_code', 'neighborhood')


@admin.register(models.Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('user', 'personal_homepage', 'phone_number',)
    list_filter = ('user', 'personal_homepage', 'phone_number',)


@admin.register(models.Birthday)
class AdminBirthday(admin.ModelAdmin):
    list_display = ('user', 'day', 'month', 'year',)
    list_filter = ('user', 'day', 'month', 'year',)


@admin.register(models.ExtendedUser)
class AdminExtendedtUser(admin.ModelAdmin):
    list_display = ('user', 'sex', 'nationality', 'user_type',)
    list_filter = ('user', 'sex', 'nationality', 'user_type',)


@admin.register(models.Facebookauth)
class AdminFacebook(admin.ModelAdmin):
    list_display = ('user', 'profile_url', 'network_username',)


@admin.register(models.Googleauth)
class AdminGoogle(admin.ModelAdmin):
    list_display = ('user', 'profile_url', 'network_username',)


@admin.register(models.Twitterauth)
class AdminTwitter(admin.ModelAdmin):
    list_display = ('user', 'profile_url', 'network_username',)

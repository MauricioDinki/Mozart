#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import ExtendedUser, Contact, Address, Birthday


@admin.register(ExtendedUser)
class AdminMozartUser(admin.ModelAdmin):
    list_display = ('user', 'sex', 'nationality', 'user_type',)
    list_filter = ('user', 'sex', 'nationality', 'user_type',)


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('user', 'personal_homepage', 'phone_number',)
    list_filter = ('user', 'personal_homepage', 'phone_number',)


@admin.register(Birthday)
class AdminDateBirth(admin.ModelAdmin):
    list_display = ('user', 'day', 'month', 'year',)
    list_filter = ('user', 'day', 'month', 'year',)


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'zip_code', 'neighborhood')

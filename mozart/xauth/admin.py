#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import ExtendUserSocialAuth


@admin.register(ExtendUserSocialAuth)
class AdminSocialUserName(admin.ModelAdmin):
    list_display = ('user', 'network_username')

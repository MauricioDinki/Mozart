#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'place',)
    prepopulated_fields = {'slug': ('name',)}

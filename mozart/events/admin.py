#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'place',)
    prepopulated_fields = {'slug': ('name',)}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Work)
class AdminWork(admin.ModelAdmin):
    list_display = ('title', 'category', 'date',)
    list_filter = ('category', 'date', )
    prepopulated_fields = {"slug": ("title",)}

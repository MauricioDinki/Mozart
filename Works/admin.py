# -*- encoding: utf-8 -*-

from .models import Work
from django.contrib import admin

@admin.register(Work)
class AdminWork(admin.ModelAdmin):
    list_display = ('title','category','date',)
    list_filter = ('category','date',)
    prepopulated_fields = {"slug": ("title",)}

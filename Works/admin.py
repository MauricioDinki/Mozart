# -*- encoding: utf-8 -*-

from django.contrib import admin

from Works.models import Work


@admin.register(Work)
class AdminWork(admin.ModelAdmin):
    list_display = ('title', 'category', 'date',)
    list_filter = ('category', 'date', )
    prepopulated_fields = {"slug": ("title",)}

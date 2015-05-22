# -*- encoding: utf-8 -*-

from django.contrib import admin

from Events.models import Event


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'place',)
    prepopulated_fields = {'slug': ('name',)}

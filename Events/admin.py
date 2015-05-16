# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Event

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
	exclude = ('slug',)
	list_display = ('name', 'place',)

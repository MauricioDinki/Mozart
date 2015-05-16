# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Event
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
	exclude = ('slug',)
	list_display = ('name', 'place',)

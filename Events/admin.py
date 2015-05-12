# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Event

@admin.register(Event)
class AdminWork(admin.ModelAdmin):
	pass
    # list_display = ('')
    # list_filter = ('')
    # prepopulated_fields = {''}

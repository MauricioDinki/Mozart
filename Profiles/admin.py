# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Artist

@admin.register(Artist)
class AdminWork(admin.ModelAdmin):
	pass

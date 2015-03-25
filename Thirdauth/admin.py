# -*- encoding: utf-8 -*-

from .models import ExtendUserSocialAuth
from django.contrib import admin

@admin.register(ExtendUserSocialAuth)
class AdminSocialUserName(admin.ModelAdmin):
	list_display = ('user','username_identificator')

# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import SocialUserName

@admin.register(SocialUserName)
class AdminSocialUserName(admin.ModelAdmin):
    list_display = ('user','facebook','twitter','google')

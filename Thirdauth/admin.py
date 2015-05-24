# -*- encoding: utf-8 -*-

from django.contrib import admin

from Thirdauth.models import ExtendUserSocialAuth


@admin.register(ExtendUserSocialAuth)
class AdminSocialUserName(admin.ModelAdmin):
    list_display = ('user', 'username_identificator')

from django.contrib import admin
from .models import Work

@admin.register(Work)
class AdminWork(admin.ModelAdmin):
    list_display = ('title','category','date',)
    list_filter = ('category','date',)
    prepopulated_fields = {"slug": ("title",)}
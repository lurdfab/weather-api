from django.contrib import admin
from .models import Description

# Register your models here.

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("weather_description", "temperature", "created_at")

admin.site.register(Description, DescriptionAdmin)
from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'file_name', 'file_location', 'created_at']


# Register your models here.
admin.site.register(File, FileAdmin)

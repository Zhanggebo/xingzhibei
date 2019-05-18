from django.contrib import admin

# Register your models here.
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ['banner_describe', 'add_time', 'isDelete']

admin.site.register(Ad, AdAdmin)
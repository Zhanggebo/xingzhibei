from django.contrib import admin

# Register your models here.
from .models import Ad

admin.site.site_title = "后台管理——星之贝"
admin.site.site_header = "星之贝后台管理"


class AdAdmin(admin.ModelAdmin):
    list_display = ['banner_describe', 'add_time', 'isDelete']

admin.site.register(Ad, AdAdmin)
from django.contrib import admin

# Register your models here.
from .models import Banner
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'baner_describe', 'add_time', 'isDelete']

admin.site.register(Banner, BannerAdmin)

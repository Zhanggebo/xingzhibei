from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ad
# Register your models here.


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    # 必须加这行 否则访问编辑页面会报错

    readonly_fields = ('banner_imamge_url',)
    list_display = ['banner_imamge_url', 'banner_describe', 'add_time', 'isDelete']


from django.contrib import admin
from .models import GoodsType,GoodsInfo
# Register your models here.

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name', 'isDelete']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'goods_name', 'goods_price', 'goods_click', 'isDelete']

admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)

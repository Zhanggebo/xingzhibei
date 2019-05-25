

from django.contrib import admin
from .models import GoodsType,GoodsInfo

from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name', 'isDelete']



# class ProxyResource(resources.ModelResource):
#     class Meta:
#         model = GoodsInfo
@admin.register(GoodsInfo)
class GoodsInfoAdmin(ImportExportModelAdmin):
    # resource_class = ProxyResource
    list_per_page = 15
    list_display = ['id', 'goods_name', 'goods_price', 'goods_click', 'isDelete']

from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(GoodsCategoryBrand)
class GoodsCategoryBrandAdmin(admin.ModelAdmin):
    readonly_fields = ('banner_imamge_url',)
    list_display = ['name', 'banner_imamge_url']


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ['parent_category', 'name', 'desc']
    list_filter = ['category_type', 'parent_category']


@admin.register(GoodsInfo)
class GoodsInfoAdmin(ImportExportModelAdmin):
    list_per_page = 15
    list_display = ['id', 'goods_name', 'goods_old_price', 'goods_price', 'goods_type', 'goods_click', 'is_recommend',
                    'isDelete']


@admin.register(GoodComment)
class GoodCommentAdmin(ImportExportModelAdmin):
    list_per_page = 15
    list_display = ['content', 'add_time']

from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'college_name']


@admin.register(DormitoryBuilding)
class DormitoryBuildingAdmin(admin.ModelAdmin):
    list_display = ['id', 'dormitory_building_name']

@admin.register(Dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'dormitory_num']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_sno', 'add_time']


@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    readonly_fields = ('imamge_url',)
    list_display = ['user', 'imamge_url']


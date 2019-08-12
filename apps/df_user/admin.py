from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'college_name']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_sno', 'add_time']


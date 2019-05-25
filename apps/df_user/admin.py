from django.contrib import admin

from .models import College, UserProfile
# Register your models here.


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'college_name']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user_sno', 'user_name', 'add_time']

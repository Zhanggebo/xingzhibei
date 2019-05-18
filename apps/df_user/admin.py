from django.contrib import admin

from .models import College, UserProfile
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'college_name']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_sno', 'user_name', 'add_time']



admin.site.register(College, CollegeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

# 学院
class College(models.Model):
    college_name = models.CharField(max_length=30, verbose_name='学院名')

    class Meta:
        verbose_name = '学院'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.college_name


# 用户信息
class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    user_name = models.CharField(max_length=30, null=True, blank=True, default='张三', verbose_name='姓名')
    user_college = models.ForeignKey(College, blank=True, verbose_name='学院', on_delete=models.CASCADE, null=True)
    user_sno = models.CharField(max_length=20, verbose_name='学号')
    user_pwd = models.CharField(max_length=30, verbose_name='密码')
    user_mobile = models.CharField(verbose_name='手机', max_length=12, null=True, blank=True)
    user_mail = models.CharField(max_length=30, null=True, blank=True, verbose_name='邮箱')
    user_address = models.CharField(max_length=100, verbose_name='地址', null=True, blank=True)

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='用户添加时间')

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_sno

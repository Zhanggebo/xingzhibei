from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 用户信息
class UserProfile(AbstractUser):

    user_sno = models.CharField(max_length=20, verbose_name='学号')
    user_name = models.CharField(max_length=30, null=True, blank=True, default='张三', verbose_name='姓名')
    user_pwd = models.CharField(max_length=30, verbose_name='密码')
    user_mail = models.CharField(max_length=30, verbose_name='邮箱')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='用户添加时间')


    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name
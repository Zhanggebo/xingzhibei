from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.html import format_html

from apps.df_goods.models import GoodsInfo
# Create your models here.

# 学院
class College(models.Model):
    college_name = models.CharField(max_length=30, verbose_name='学院名')

    class Meta:
        verbose_name = '学院'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.college_name

# 宿舍楼
class DormitoryBuilding(models.Model):
    dormitory_building_name = models.CharField(max_length=30, verbose_name='宿舍楼')
    class Meta:
        verbose_name = '宿舍楼'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dormitory_building_name


# 宿舍
class Dormitory(models.Model):
    dormitory_num = models.CharField(max_length=30, verbose_name='宿舍号')
    class Meta:
        verbose_name = '宿舍号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dormitory_num


# 用户信息
class UserProfile(models.Model):
    user_name = models.CharField(max_length=30, null=True, blank=True, default='张三', verbose_name='姓名')
    user_college = models.ForeignKey(College, blank=True, verbose_name='学院', on_delete=models.CASCADE, null=True)
    user_sno = models.CharField(max_length=20, verbose_name='学号')
    user_pwd = models.CharField(max_length=30, verbose_name='密码')
    user_mobile = models.CharField(verbose_name='手机', max_length=12, null=True, blank=True)
    user_mail = models.CharField(max_length=30, null=True, blank=True, verbose_name='邮箱')
    user_dormitory_building = models.ForeignKey(DormitoryBuilding, blank=True, verbose_name='宿舍楼', on_delete=models.CASCADE, null=True)
    user_dormitory_num = models.ForeignKey(Dormitory, blank=True, verbose_name='宿舍号', on_delete=models.CASCADE, null=True)
    user_address = models.CharField(max_length=100, verbose_name='地址', null=True, blank=True)
    user_remark = models.CharField(max_length=30, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='用户添加时间')

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_sno


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, verbose_name='用户', on_delete=models.CASCADE, null=True)
    good = models.ForeignKey(GoodsInfo, blank=True, verbose_name='商品', on_delete=models.CASCADE, null=True)

    def imamge_url(self):
        return format_html( '<img src="{0}" width="100px"/>', self.good.goods_pic.url)
    imamge_url.short_description = '产品图片'

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__()
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Ad(models.Model):
    banner_imamge = models.ImageField(verbose_name='图片', upload_to='banners/%Y/%m', blank=True)
    banner_describe = models.CharField(verbose_name='图片描述', max_length=32, default='广告位招租')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='商品添加时间')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    def banner_imamge_url(self):
        print(self.banner_imamge)
        return format_html( '<img src="{0}" width="100px"/>', self.banner_imamge.url)
    banner_imamge_url.short_description = u'图片'


    class Meta:
        verbose_name = '主页Banner'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.banner_describe





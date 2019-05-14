from django.db import models
from datetime import datetime

# Create your models here.


# Banner
class Banner(models.Model):
    banner_imamge = models.ImageField(verbose_name='图片', upload_to='banners/%Y/%m', blank=True)
    baner_describe = models.CharField(verbose_name='图片描述', max_length=32, default='广告位招租')
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '主页Banner'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.baner_describe
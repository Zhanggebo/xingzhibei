from django.db import models
from django.utils.html import format_html
from datetime import datetime
from apps.df_goods.models import GoodsInfo
# Create your models here.

class Message(models.Model):
    user_name = models.CharField(verbose_name='用户名', max_length=32)
    message = models.CharField(verbose_name='留言', max_length=126)
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


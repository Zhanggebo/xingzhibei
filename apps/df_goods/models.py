from django.db import models
from tinymce.models import HTMLField
# Create your models here.

# 商品类型
class GoodsType(models.Model):
    type_name = models.CharField(max_length=30, verbose_name='类型名称')
    type_imamge = models.ImageField(upload_to='goodstype/%Y/%m', blank=True, verbose_name='类型图片')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


# 商品信息
class GoodsInfo(models.Model):
    DEGREE = (
        ('9', '9成'),
        ('8', '前端'),
        ('7', '日记'),
        ('6', 'Linux'),
        ('5', '5成以下'),
    )

    goods_name = models.CharField(max_length=30, verbose_name='商品名称')
    goods_detail = models.CharField(max_length=200, verbose_name='商品描述')
    goods_degree = models.CharField(verbose_name='商品新旧程度', choices=DEGREE, max_length=16)
    goods_introduce = HTMLField(verbose_name='商品介绍页')

    goods_pic = models.ImageField(upload_to='goods/%Y/%m', blank=True, verbose_name='商品图片')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')
    goods_click = models.IntegerField(verbose_name='商品人气', default=0)

    goods_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name='商品类型')

    isDelete = models.BooleanField(default=False, verbose_name='是否删除')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='商品添加时间')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name
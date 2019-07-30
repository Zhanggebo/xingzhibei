from datetime import datetime

from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html
# Create your models here.


# 商品类别
class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )

    name = models.CharField(default='', max_length=30, verbose_name='类别名', help_text='类别名')
    code = models.CharField(default='', max_length=30, verbose_name='类别code', help_text='类别code')
    desc = models.TextField(default='', verbose_name='类别描述', help_text='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='类目级别', help_text='类目级别')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父类目级别',related_name='sub_cat', help_text='父目录', on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(default='', max_length=30, verbose_name='品牌名', help_text='品牌名')
    desc = models.TextField(default='', max_length=200, verbose_name='品牌描述', help_text='品牌描述')
    image = models.ImageField(max_length=200, upload_to='brand/%Y/%m')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def banner_imamge_url(self):
        print(self.image)
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    banner_imamge_url.short_description = u'图片'

    class Meta:
        verbose_name = '品牌名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 商品信息
class GoodsInfo(models.Model):
    DEGREE = (
        ('9', '9成'),
        ('8', '8成'),
        ('7', '7成'),
        ('6', '6成'),
        ('5', '5成以下'),
    )

    TYPE = (
        ('costume','服饰配饰'),
        ('electronics','数码科技'),
        ('sport','运动代步'),
        ('stationery','书籍文具'),
        ('game','虚拟产品'),
        ('other','其他'),
    )
    goods_pic = models.ImageField(upload_to='goods/%Y/%m', blank=True, verbose_name='商品图片')
    goods_name = models.CharField(max_length=30, verbose_name='商品名称')
    goods_detail = models.CharField(max_length=200, verbose_name='商品描述')
    goods_degree = models.CharField(verbose_name='商品新旧程度', choices=DEGREE, max_length=16)
    goods_introduce = HTMLField(verbose_name='商品介绍页')
    goods_old_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品原价(￥)', default=100)
    goods_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格(￥)')
    goods_click = models.IntegerField(verbose_name='商品人气', default=0)

    # 暂时注释,不做动态添加
    # goods_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name='商品类型')
    goods_type = models.CharField(max_length=16, choices=TYPE, verbose_name='商品类型')

    isDelete = models.BooleanField(default=False, verbose_name='是否删除')
    is_recommend = models.BooleanField(default=False, verbose_name='首页推荐')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='商品添加时间')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name

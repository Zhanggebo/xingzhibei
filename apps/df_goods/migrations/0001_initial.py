# Generated by Django 2.1 on 2019-05-25 14:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(blank=True, upload_to='goods/%Y/%m', verbose_name='商品图片')),
                ('goods_name', models.CharField(max_length=30, verbose_name='商品名称')),
                ('goods_detail', models.CharField(max_length=200, verbose_name='商品描述')),
                ('goods_degree', models.CharField(choices=[('9', '9成'), ('8', '8成'), ('7', '7成'), ('6', '6成'), ('5', '5成以下')], max_length=16, verbose_name='商品新旧程度')),
                ('goods_introduce', tinymce.models.HTMLField(verbose_name='商品介绍页')),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='商品价格(￥)')),
                ('goods_click', models.IntegerField(default=0, verbose_name='商品人气')),
                ('goods_type', models.CharField(choices=[('costume', '服饰配饰'), ('electronics', '数码科技'), ('sport', '运动代步'), ('stationery', '书籍文具'), ('game', '虚拟产品'), ('other', '其他')], max_length=16, verbose_name='商品类型')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='商品添加时间')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30, verbose_name='类型名称')),
                ('type_imamge', models.ImageField(blank=True, upload_to='goodstype/%Y/%m', verbose_name='类型图片')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
            },
        ),
    ]

# Generated by Django 2.1 on 2019-05-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_imamge', models.ImageField(blank=True, upload_to='banners/%Y/%m', verbose_name='图片')),
                ('banner_describe', models.CharField(default='广告位招租', max_length=32, verbose_name='图片描述')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='商品添加时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '主页Banner',
                'verbose_name_plural': '主页Banner',
            },
        ),
    ]

# Generated by Django 2.1 on 2019-08-13 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0003_auto_20190813_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='good',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cls_good', to='df_goods.GoodsInfo', verbose_name='商品'),
        ),
    ]

# Generated by Django 2.1 on 2019-05-18 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_auto_20190518_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='df_user.College', verbose_name='学院'),
        ),
    ]
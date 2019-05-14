# Generated by Django 2.1 on 2019-05-11 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=30, verbose_name='学院名')),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_college',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='df_user.College', verbose_name='学院'),
            preserve_default=False,
        ),
    ]
from django.apps import AppConfig


class AdConfig(AppConfig):
    # 注册的app
    name = 'apps.ad'
    # 给注册的app后台设置中文名
    verbose_name = '广告设置'

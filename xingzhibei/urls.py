"""xingzhibei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include



admin.site.site_title = "后台管理——星之贝"
admin.site.site_header = "星之贝后台管理"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.df_goods.urls', namespace='goods')),
    path('user/', include('apps.df_user.urls' ,namespace='user')),
    path('site_config/', include('apps.site_config.urls' ,namespace='site_config')),

    # 富文本编辑器url
    path('tinymce/', include('tinymce.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 全局配置404
handler404 = 'apps.site_config.page404.'
# handler500 = 'users.views.page_error'
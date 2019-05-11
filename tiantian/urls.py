"""tiantian URL Configuration

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
from django.contrib import admin
from django.urls import path, include


from django.views.generic import View
from django.shortcuts import render

class Index(View):
    def get(self, request):
        is_login = request.session.get('is_login', None)
        print(request.session.get('is_login', None))
        print(request.session.get('user_sno', None))
        return render(request, 'index.html', {'is_login': is_login})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('user/', include('apps.df_user.urls' ,namespace='user')),
]

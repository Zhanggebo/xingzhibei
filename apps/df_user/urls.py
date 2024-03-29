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
from django.urls import path

from .views import Register, Login, logout ,Cart, UserCenterInfo, UserCenterOrder,UserCenterSite

app_name = 'user'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),


    path('cart/', Cart.as_view(), name='cart'),



    path('user_center_info/', UserCenterInfo.as_view(), name='user_center_info'),
    path('user_center_order/', UserCenterOrder.as_view(), name='user_center_order'),
    path('user_center_site/', UserCenterSite.as_view(), name='user_center_site'),


]

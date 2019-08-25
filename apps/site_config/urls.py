
from django.urls import path

from .views import *

app_name = 'site_config'

urlpatterns = [
    path('about_us/', AboutUs.as_view(), name='about_us'),

]

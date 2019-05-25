from django.shortcuts import render
from django.views.generic import View

from apps.ad.models import Ad
from .models import GoodsType,GoodsInfo

# Create your views here.

class Index(View):
    def get(self, request):
        # 主页配置开始

        # 广告
        all_ads = Ad.objects.all().filter(isDelete=False)[:3]

        return render(request, 'index.html', {
            'all_ads': all_ads,
        })


class Detail(View):

    def get(self,request):
        return render(request, 'detail.html')

class List(View):

    def get(self,request,classify):

        return render(request, 'list.html')


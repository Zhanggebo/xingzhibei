from django.shortcuts import render
from django.views.generic import View

from apps.ad.models import Ad
from .models import GoodsType,GoodsInfo

# Create your views here.

class Index(View):
    def get(self, request):
        is_login = request.session.get('is_login', None)
        user_sno = request.session.get('user_sno', None)
        print(request.session.get('is_login', None))
        print(request.session.get('user_sno', None))

        # 主页配置开始

        # 广告
        all_ads = Ad.objects.all().filter(isDelete=False)[:3]


        return render(request, 'index.html', {
            'is_login': is_login,
            'user_sno': user_sno,
            'all_ads': all_ads,
        })


class Detail(View):

    def get(self,request):
        return render(request, 'detail.html')

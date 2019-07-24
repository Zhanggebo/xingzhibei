from django.shortcuts import render
from django.views.generic import View

from apps.ad.models import Ad
from apps.df_goods.models import GoodsCategory
# Create your views here.

class Index(View):
    def get(self, request):
        # 广告
        all_ads = Ad.objects.all().filter(isDelete=False)[:3]
        # 主页配置开始
        # 获取所有的商品类型
        all_dress = GoodsCategory.objects.get(code='dress').sub_cat.all()
        all_electric = GoodsCategory.objects.get(code='electric').sub_cat.all()

        return render(request, 'index.html', {
            'all_ads': all_ads,
            'all_dress': all_dress,
        })


class Detail(View):

    def get(self,request):
        return render(request, 'detail.html')


class List(View):

    def get(self,request,classify):
        all_dress = GoodsCategory.objects.get(code=classify).sub_cat.all()
        print(all_dress)
        return render(request, 'list.html')


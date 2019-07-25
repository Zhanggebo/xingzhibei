from django.shortcuts import render
from django.views.generic import View

from apps.ad.models import Ad
from apps.df_goods.models import GoodsCategory, GoodsInfo


# Create your views here.

class Index(View):
    def get(self, request):
        # 广告
        all_ads = Ad.objects.all().filter(isDelete=False)[:3]
        # 主页配置开始
        # 获取所有的商品类型
        all_dress_classify = GoodsCategory.objects.get(code='dress').sub_cat.all()
        all_electric = GoodsCategory.objects.get(code='electric').sub_cat.all()

        # 获取所有的商品
        all_goods = GoodsInfo.objects.all()
        recommend_dress = all_goods.filter(goods_type='costume', is_recommend=True)[:4]
        recommend_electronics = all_goods.filter(goods_type='electronics', is_recommend=True)[:4]

        return render(request, 'index.html', {
            'all_ads': all_ads,
            'all_dress_classify': all_dress_classify,

            'recommend_dress': recommend_dress,
            'recommend_electronics': recommend_electronics
        })


class Detail(View):

    def get(self, request):
        good_id = request.GET.get('good_id', '')
        good = GoodsInfo.objects.get(id=good_id)

        return render(request, 'detail.html', {
            'good': good
        })


class List(View):

    def get(self, request, classify):
        all_dress = GoodsCategory.objects.get(code=classify).sub_cat.all()
        print(all_dress)
        return render(request, 'list.html')

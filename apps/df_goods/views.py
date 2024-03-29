from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from apps.ad.models import Ad
from apps.df_goods.models import GoodsCategory, GoodsInfo
from pure_pagination import PageNotAnInteger,Paginator,EmptyPage

# Create your views here.

class Index(View):
    def get(self, request):
        # 广告
        all_ads = Ad.objects.all().filter(isDelete=False)[:3]
        # 主页配置开始
        # 获取所有的商品类型
        all_dress_classify = GoodsCategory.objects.get(code='dress').sub_cat.all()
        all_electric = GoodsCategory.objects.get(code='electric').sub_cat.all()

        # 获取所有的商品，筛选首页推荐产品
        all_goods = GoodsInfo.objects.all()
        recommend_dress = all_goods.filter(goods_type='costume', is_recommend=True)[:4]
        recommend_electronics = all_goods.filter(goods_type='electronics', is_recommend=True)[:4]
        recommend_sports = all_goods.filter(goods_type='sport', is_recommend=True)[:4]
        recommend_stationery = all_goods.filter(goods_type='stationery', is_recommend=True)[:4]
        recommend_game = all_goods.filter(goods_type='game', is_recommend=True)[:4]
        recommend_other = all_goods.filter(goods_type='other', is_recommend=True)[:4]


        return render(request, 'index.html', {
            'all_ads': all_ads,
            'all_dress_classify': all_dress_classify,

            'recommend_dress': recommend_dress,
            'recommend_electronics': recommend_electronics,
            'recommend_sports':recommend_sports,
            'recommend_stationery':recommend_stationery,
            'recommend_game':recommend_game,
            'recommend_other':recommend_other,

        })


# 商品详情页
class Detail(View):
    def get(self, request):
        good_id = request.GET.get('good_id','')
        good = GoodsInfo.objects.get(id=good_id)

        good_type = good.goods_type  #取出类型
        good_type = GoodsInfo.objects.filter(goods_type=good_type)[:3]  #按类型查找

        good.goods_click += 1        #点击商品人气+1
        good.save()


        return render(request, 'detail.html', {
            'good': good,
            'good_ty':good_type
        })




# 商品列表页
class List(View):

    def get(self, request, classify):

        # all_goods = GoodsCategory.objects.filter(code=classify).sub_cat.all()
        if classify == 'all':
            all_goods = GoodsInfo.objects.all()
        else:
            all_goods = GoodsInfo.objects.filter(goods_type=classify)

        #商品排序
        sort = request.GET.get('sort',"")
        if sort:
            if sort == "goods_price":
                all_goods = all_goods.order_by("-goods_price")  #价格排序
            elif sort == "goods_click":
                all_goods = all_goods.order_by("-goods_click")  #人气排序

        all_good_s = all_goods.order_by("-add_time")  # 日期排序


        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        #每页显示数量
        p = Paginator(all_goods, 5)
        all_goods = p.page(page)

        return render(request, 'list.html',{
            'all_goods':all_goods,
            'sort':sort,  #商品排序增加的
            'all_good_s':all_good_s,

        })


# 搜索
class Search(View):
    def get(self, request):

        keyboard = request.GET.get('keyboard','')
        search_goods = GoodsInfo.objects.all()
        if keyboard:
            search_goods = search_goods.filter(Q(goods_name__contains=keyboard) )
        # 前期分页没弄好 放在后期
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 每页显示数量
        p = Paginator(search_goods, 100)
        search_goods = p.page(page)
        return render(request, 'search.html', {'search_goods': search_goods})
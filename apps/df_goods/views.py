from django.shortcuts import render
from django.views.generic import View

from .models import GoodsType,GoodsInfo
# Create your views here.

class Index(View):
    def get(self, request):
        is_login = request.session.get('is_login', None)
        print(request.session.get('is_login', None))
        print(request.session.get('user_sno', None))

        # 主页配置开始
        all_goods_type = GoodsType.objects.all()

        return render(request, 'index.html', {
            'is_login': is_login,
            'all_goods_type': all_goods_type,
        })

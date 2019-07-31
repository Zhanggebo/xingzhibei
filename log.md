# 王皇更新日志

##商品列表 中：  价格  人气  排序
    			<a href="#" class="{% if sort == '' %}active{% endif %}">默认</a>
				<a href="?sort=goods_price" class="{% if sort == 'goods_price' %}active{% endif %}">价格</a> <!--2019/7/31-->
				<a href="?sort=goods_click" class="{% if sort == 'goods_click' %}active{% endif %}">人气</a>     <!--2019/7/31-->
                        #商品排序
                sort = request.GET.get('sort',"")
                if sort:
                    if sort == "goods_price":
                        all_goods = all_goods.order_by("-goods_price")
                    elif sort == "goods_click":
                        all_goods = all_goods.order_by("-goods_click")





# 董国伟更新日志
1. 2019/07/26
> 对什么url.py文件加入XXXX

2. 2019/07/30
> 基本完成首页,商品列表页,超链接
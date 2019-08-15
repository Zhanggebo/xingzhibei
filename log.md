# 王皇更新日志

##商品列表 中：  价格  人气  排序
```python
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
```
2019/8/1
>商品点击+1

2019/8/2
>新品推荐  按添加日期显示
>分页做完了

2019/8/3
>闲置宝贝推荐 按商品类型 处理

2019/8/15
>商品搜索   后期在制作分页显示 



# 董国伟更新日志
1. 2019/07/26
> 对什么url.py文件加入XXXX

2. 2019/07/30
> 基本完成首页,商品列表页,超链接

3. 2019/08/09
> 重构user用户配置,将用户添加商品的功能移至django自带的后台
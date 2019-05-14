# **********************OBJ INFO**************************
# Author:Kali Yu
# @Time    : 2019-5-14 21:46
# @Site    : 52ziyu.cn
# @File    : user_decorator.py
# @software: PyCharm
# *********************************************************



from django.http import HttpResponseRedirect


# 登录装饰器
def login(func):
    # 这里的self是站位符,用于接收类属性中的self的,不能删
    def login_fun(self,request,*args,**kwargs):
        if request.session.get('is_login'):
            return func(self,request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            # 这里用户可能在不同地方,获取登录
            # 登录成功后我们想返回,点的地方
            # get_full_path 返回完整的路径
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun
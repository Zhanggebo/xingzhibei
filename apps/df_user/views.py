from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .models import UserProfile,College

from . import user_decorator

from hashlib import sha1

# Create your views here.

# 注册
class Register(View):

    def get(self, request):
        return render(request, 'df_user/register.html')

    # 处理注册请求
    def post(self, request):
        user_sno = request.POST.get('user_name')
        user_pwd =request.POST.get('pwd')
        user_cpwd =request.POST.get('cpwd')
        user_mail =request.POST.get('email')

        # 判断用户是否存在
        if  UserProfile.objects.filter(user_sno=user_sno):
            msg = '<h1>用户名已经存在</h1>'
            return HttpResponse(msg)
        # 判断两次密码
        if user_pwd=='' or user_pwd!=user_cpwd:
            msg = '<h1>两次密码不一致</h1>'
            return HttpResponse(msg)
        # 判断邮箱是否正确
        from django.core.validators import validate_email
        try:
            validate_email(user_mail)
        except:
            msg = '<h1>请输入正确邮箱</h1>'
            return HttpResponse(msg)


        # 加密password进行保存
        # user_profile.password = make_password(pass_word)
        # user_profile.save()

        # 密码加密
        # s1 = sha1()
        # s1.update(user_pwd)
        # upwd3 = s1.hexdigest()

        # 创建对象
        user = UserProfile()
        user.user_sno = user_sno
        user.user_pwd = user_pwd
        user.user_mail = user_mail
        user.save()
        # 注册成功
        return render(request, 'df_user/login.html', {
            'user_sno': user_sno,
        })
        # return redirect('/user/login/')

# 登录
class Login(View):

    def get(self, request):
        return render(request, 'df_user/login.html')

    def post(self, request):
        user_sno = request.POST.get('username')
        user_pwd = request.POST.get('pwd')

        # 判断用户是否存在
        user = UserProfile.objects.filter(user_sno=user_sno)
        if  not user:
            msg = '用户名不存在'
            print(user)
            return render(request, 'df_user/login.html', {
                'error_msg': msg,
            })

        # 判断用户密码是否正确
        if user_pwd != user[0].user_pwd:
            msg = '用户名密码错误'
            return render(request, 'df_user/login.html', {
                'error_msg': msg,
            })

        # 登录成功设置session
        request.session['is_login'] = True
        request.session['user_sno'] = user_sno
        request.session['user_name'] = user[0].user_name
        request.session['user_id'] = user[0].id
        return redirect('/')

# 登出
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/user/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/user/login/")


# 用户

class Cart(View):

    @user_decorator.login
    def get(self, request):
        return render(request, 'df_user/cart.html')


class UserCenterInfo(View):
    @user_decorator.login
    def get(self, request):
        # 获取当前用户的信息
        user_sno = request.session.get('user_sno')
        user = UserProfile.objects.filter(user_sno=user_sno)
        user_colege = user[0].user_college
        user_sno = user[0].user_sno
        user_name = user[0].user_name
        user_mobile = user[0].user_mobile
        user_address = user[0].user_address

        # 获取所有学院
        all_colleges = College.objects.all().order_by('-id')
        context = {
            'user_colege': user_colege,
            'user_sno': user_sno,
            'user_name': user_name,
            'user_mobile': user_mobile,
            'user_address': user_address,
            'all_colleges': all_colleges,
        }
        return render(request, 'df_user/user_center_info.html', context)

    def post(self, request):
        # 获取提交过来的信息
        user_colloge_id = request.POST.get('user_colloge_id')
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        user_mobile = request.POST.get('user_mobile')
        # 找到这个用户
        user = UserProfile.objects.filter(id=user_id)
        user.update(user_college=user_colloge_id, user_name=user_name, user_mobile=user_mobile)
        return HttpResponse('ok')

class UserCenterOrder(View):

    @user_decorator.login
    def get(self, request):

        return render(request, 'df_user/user_center_order.html')

class UserCenterSite(View):
    @user_decorator.login
    def get(self, request):
        return render(request, 'df_user/user_center_site.html')


from django.core.validators import RegexValidator
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from apps.df_user.forms import RegisterForm
from .models import *

from . import user_decorator

from hashlib import sha1


# 注册
class Register(View):

    def get(self, request):
        return render(request, 'df_user/register.html')

    # 处理注册请求
    # def post(self, request):
    #     register_form = RegisterForm(request.POST)
    #     if register_form.is_valid():
    #         user_name = request.POST.get('name')
    #         user_sno = request.POST.get('user_sno')
    #         user_pwd = request.POST.get('pwd')
    #         user_cpwd = request.POST.get('cpwd')
    #         user_mail = request.POST.get('email')
    #
    #         # 判断学号是否存在
    #         if UserProfile.objects.filter(user_sno=user_sno):
    #             msg = '<h1>该学号已经存在</h1>'
    #             return HttpResponse(msg)
    #
    #         # 判断两次密码
    #         if user_pwd == '' or user_pwd != user_cpwd:
    #             msg = '<h1>两次密码不一致</h1>'
    #             return HttpResponse(msg)
    #         # 判断邮箱是否正确
    #         from django.core.validators import validate_email
    #         try:
    #             validate_email(user_mail)
    #         except:
    #             msg = '<h1>请输入正确邮箱</h1>'
    #             return HttpResponse(msg)
    #
    #         # 加密password进行保存
    #         # user_profile.password = make_password(pass_word)
    #         # user_profile.save()
    #
    #         # 密码加密
    #         # s1 = sha1()
    #         # s1.update(user_pwd)
    #         # upwd3 = s1.hexdigest()
    #
    #         # 创建对象
    #         user = UserProfile()
    #         user.user_name = user_name
    #         user.user_sno = user_sno
    #         user.user_pwd = user_pwd
    #         user.user_mail = user_mail
    #         user.save()
    #         # 注册成功
    #         return render(request, 'df_user/login.html', {
    #             'user_sno': user_sno,
    #         })
    #         # return redirect('/user/login/')
    #     else:
    #         msg = '<h1>请输入正确学号</h1>'
    #         return HttpResponse(msg)

    #  原来的可以取消注释
    def post(self, request):
        error_msg = {}
        user_name = request.POST.get('user_name')
        user_sno = request.POST.get('user_sno')
        user_pwd = request.POST.get('pwd')
        user_cpwd = request.POST.get('cpwd')
        user_mail = request.POST.get('email')
        # 判断学号是否正确以及存在
        if not user_sno.isdigit():
            error_msg['user_sno'] = '亲,学号是数字哦'
        if UserProfile.objects.filter(user_sno=user_sno):
            error_msg['user_sno'] = '亲,该学号已经存在,可联系工作人员进行实名审核哦'
        if len(user_sno)<8 or len(user_sno)>11 :
            error_msg['user_sno'] = '请输入8-11位的学号'

        # 判断两次密码
        if user_pwd == '' or user_pwd != user_cpwd:
            error_msg['user_pwd'] = '两次密码不一致'
        # 判断邮箱是否正确
        from django.core.validators import validate_email
        try:
            validate_email(user_mail)
        except:
            error_msg['user_mail'] = '请输入正确邮箱'

        if not error_msg:
            # 创建对象
            user = UserProfile()
            user.user_name = user_name
            user.user_sno = user_sno
            user.user_pwd = user_pwd
            user.user_mail = user_mail
            user.save()
            # 注册成功
            return render(request, 'df_user/login.html', {
                'user_sno': user_sno,
            })
        else:
            print(error_msg)
            return render(request, 'df_user/register.html', {'error_msg': error_msg})


# 登录
class Login(View):

    def get(self, request):
        return render(request, 'df_user/login.html')

    def post(self, request):
        user_sno = request.POST.get('user_sno')
        user_pwd = request.POST.get('pwd')

        # 判断用户是否存在
        user = UserProfile.objects.filter(user_sno=user_sno)
        if not user:
            msg = '用户名不存在'
            return render(request, 'df_user/login.html', {
                'error_msg': msg,
            })

        # 判断用户密码是否正确
        if user_pwd != user[0].user_pwd:
            msg = '用户名密码错误'
            return render(request, 'df_user/login.html', {
                'error_msg': msg,
            })

        # 获取用户收藏的产品
        user_fav_products_num = UserFavorite.objects.filter(user=user[0].id).count()

        # 登录成功设置session
        request.session['is_login'] = True
        request.session['user_sno'] = user_sno
        request.session['user_name'] = user[0].user_name
        request.session['user_id'] = user[0].id
        request.session['user_fav_products_num'] = user_fav_products_num
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


# 用户收藏
class Cart(View):

    @user_decorator.login
    def get(self, request):
        # 获取当前用户收藏的商品
        user_sno = request.session.get('user_sno')
        user_fav = UserFavorite.objects.filter(user__user_sno=user_sno)

        # del_good_id = request.GET.get('del_good_id')
        # user = UserFavorite.objects.filter(user__user_sno=user_sno)
        # print(user[0].good.id)

        return render(request, 'df_user/cart.html', {
            'user_fav': user_fav
        })

    def post(self, request):
        # 添加收藏商品
        user_id = request.session.get('user_id')
        good_id = request.POST.get('good_id')
        user_sno = request.session.get('user_sno')
        if user_id:
            # 下一步判断用户是否已经添加过
            is_in_good = UserFavorite.objects.filter(user__user_sno=user_sno)
            # 该用户收藏为0的话
            user_fav = UserFavorite()
            user_fav.user_id = user_id
            user_fav.good_id = good_id
            user_fav.save()
        return redirect('/')


# 用户信息
class UserCenterInfo(View):
    @user_decorator.login
    def get(self, request):
        # 获取当前用户的信息
        user_sno = request.session.get('user_sno')
        user = UserProfile.objects.filter(user_sno=user_sno)[0]
        user_colege = user.user_college
        user_sno = user.user_sno
        user_name = user.user_name
        user_mobile = user.user_mobile
        user_address = user.user_address
        user_dormitory_building_name = user.user_dormitory_building
        user_dormitory_num = user.user_dormitory_num
        user_remark = user.user_remark

        # 获取所有学院,宿舍楼,宿舍号
        all_colleges = College.objects.all().order_by('-id')
        all_dormitory_buildings = DormitoryBuilding.objects.all().order_by('-id')
        all_dormitories = Dormitory.objects.all().order_by('-id')
        context = {
            'user_colege': user_colege,
            'user_sno': user_sno,
            'user_name': user_name,
            'user_mobile': user_mobile,
            'user_address': user_address,
            'user_dormitory_building_name': user_dormitory_building_name,
            'all_colleges': all_colleges,
            'all_dormitory_buildings': all_dormitory_buildings,
            'user_dormitory_num': user_dormitory_num,
            'user_remark': user_remark,
            'all_dormitories': all_dormitories
        }
        return render(request, 'df_user/user_center_info.html', context)

    def post(self, request):
        # 获取提交过来的信息
        user_colloge_id = request.POST.get('user_colloge_id')
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        user_mobile = request.POST.get('user_mobile')
        user_dormitory_building_id = request.POST.get('dormitory_building_id')
        user_dormitory_id = request.POST.get('dormitory_id')
        user_remark = request.POST.get('user_remark')
        # 找到这个用户
        user = UserProfile.objects.filter(id=user_id)
        user.update(user_college=user_colloge_id, user_name=user_name, user_mobile=user_mobile,
                    user_dormitory_building=user_dormitory_building_id,
                    user_dormitory_num=user_dormitory_id, user_remark=user_remark)
        return HttpResponse('ok')


class UserCenterOrder(View):

    @user_decorator.login
    def get(self, request):
        return render(request, 'df_user/user_center_order.html')


class UserCenterSite(View):
    @user_decorator.login
    def get(self, request):
        return render(request, 'df_user/user_center_site.html')

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render


# 注册
from django.urls import reverse

from user.froms import UserRegisterForm, UserLoginForm, UserAddressForm
from user.models import User, UserAddress


def register(request):
    if request.method == 'GET':
        return render(request, 'web/register.html')

    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        # 校验通过
        if form.is_valid():
            password = make_password(form.cleaned_data.get('pwd'))
            User.objects.create(username=form.cleaned_data.get('user_name'), password=password)
            return HttpResponseRedirect(reverse('user:login'))
        # 验证不通过，返回错误信息
        else:
            return render(request, 'web/register.html', {'errors': form.errors})


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'web/login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data.get('username')).first()
            if not user:
                errors = '没有该用户'
                return render(request, 'web/login.html', {'errors': errors})
            if check_password(form.cleaned_data.get('pwd'), user.password):
                # request.user
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('goods:index'))
            else:
                return render(request, 'web/login.html', {'errors': '密码错误'})
        else:
            return render(request, 'web/login.html', {'errors': form.errors})


# 注销
def logout(request):
    if request.method == 'GET':
        # del request.session['user_id']
        # 清空session
        request.session.flush()
        return HttpResponseRedirect(reverse('user:login'))


def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'web/user_center_info.html')


# def user_center_order(request):
#     if request.method == 'GET':
#         return render(request, 'web/user_center_order.html')


# 用户地址
def user_center_site(request):
    # if request.method == 'GET':
    #     return render(request, 'web/user_center_site.html')
    if request.method == 'GET':
        user = request.user
        # 获取用户的收货地址信息
        user_addresses = UserAddress.objects.filter(user=user).order_by('-id')
        return render(request, 'web/user_center_site.html', {'user_addresses': user_addresses})

    if request.method == 'POST':
        # 使用表单验证，验证收货地址的参数是否填写完整
        form = UserAddressForm(request.POST)
        if form.is_valid():
            user = request.user
            address_info = form.cleaned_data
            # 保存收货地址信息
            UserAddress.objects.create(**address_info, user=user)
            # 保存成功收货地址
            return HttpResponseRedirect(reverse('user:user_center_site'))
        else:
            user = request.user
            # 获取用户的收货地址信息
            user_addresses = UserAddress.objects.filter(user=user).order_by('-id')
            return render(request, 'web/user_center_site.html', {'form': form, 'user_addresses': user_addresses})



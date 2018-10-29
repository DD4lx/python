import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.models import User, UserToken


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        sure_password = request.POST.get('sure_pwd')
        if not all([username,password]):
            msg = '用户名或密码不能为空'
            return render(request, 'register.html', {'msg': msg})
        if User.objects.filter(username=username).first():
            msg = '该用户名已被注册'
            return render(request, 'register.html', {'msg': msg})
        if password != sure_password:
            msg = '两次输入密码不一致'
            return render(request, 'register.html', {'msg': msg})
        User.objects.create(username=username, password=password)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username,password]):
            msg = '用户名或密码为空'
            return render(request, 'login.html', {'msg': msg})
        user = User.objects.filter(username=username).first()
        if not user:
            msg = '没有该用户'
            return render(request, 'login.html', {'msg': msg})
        if password != user.password:
            msg = '密码不正确'
            return render(request, 'login.html', {'msg': msg})

        # 标识符：
        # 使用请求与响应：
        # 请求：是从浏览器发送请求的时候，传递给后端的。
        # 响应：后端返回给浏览器的。
        res = HttpResponseRedirect(reverse('content:index'))
        # set_cookie(key,value,max_age)绑定了一个cookie值，实际上就是一个字典；
        # 把标识符丢给页面，浏览器会存起来
        token = ''
        s = '1234567890qazwsxedcrfvtgbyhnujmiklop'
        for i in range(25):
            token += random.choice(s)
        res.set_cookie('token', token, max_age=6000)

        # 服务器端存token数据
        user_token = UserToken.objects.filter(user=user).first()
        if not user_token:
            UserToken.objects.create(token=token, user=user)
        else:
            user_token.token = token
            user_token.save()

        return res


# 当用户再次访问content.index页面时，通过cookie就可以检测出该用户是否已经登录过了；
# 如果登录过，访问index 时就不用再登陆了，直接可以访问，如果没有登录，就需要先登录，再访问；


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.models import User, UserToken
from utils.functions import login_required


@login_required
def index(request):
    if request.method == 'GET':

        return render(request, 'index.html')


# 注销登录
@login_required
def logout(request):
    if request.method == 'GET':
        # 删除浏览器cookie中的token参数
        res = HttpResponseRedirect(reverse('user:login'))
        res.delete_cookie('token')
        # 获取浏览器中的cookie值
        token = request.COOKIES.get('token')
        # 删除数据库中的数据
        UserToken.objects.filter(token=token).delete()

        return res


# 相册
@login_required
def share(request):
    if request.method == 'GET':
        return render(request, 'share.html')


# 博客日记
@login_required
def list(request):
    if request.method == 'GET':
        return render(request, 'list.html')


# 关于我的信息
@login_required
def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


# 留言
@login_required
def gbook(request):
    if request.method == 'GET':
        return render(request, 'gbook.html')


# 内容页
@login_required
def info(request):
    if request.method == 'GET':
        return render(request, 'info.html')


# 图片内容页
@login_required
def infopic(request):
    if request.method == 'GET':
        return render(request, 'infopic.html')

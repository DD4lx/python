from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.models import Article, Category


# 首页
def index(request):
    if request.method == 'GET':
        articles = Article.objects.filter(is_delete=0)
        categorys = Category.objects.filter(is_delete=0)

        return render(request, 'web/index.html', {'articles': articles, 'categorys': categorys})


# 相册
def share(request):
    if request.method == 'GET':
        return render(request, 'web/share.html')


# 博客日记
def list(request):
    if request.method == 'GET':
        return render(request, 'web/list.html')


# 关于我的信息
def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


# 留言
def gbook(request):
    if request.method == 'GET':
        return render(request, 'web/gbook.html')


# 内容页
def info(request):
    if request.method == 'GET':
        return render(request, 'web/info.html')


# 图片内容页
def infopic(request):
    if request.method == 'GET':
        return render(request, 'web/infopic.html')


# 文章详情
def article(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(id=id).first()
        return render(request, 'web/article.html', {'article': article})

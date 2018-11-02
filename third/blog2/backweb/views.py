from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render



from django.urls import reverse

from backweb.forms import UserRegisterForm, UserLoginForm



from backweb.models import Article, Category


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')

    if request.method == 'POST':
        # 获取注册页面中输入的数据
        data = request.POST
        # 将数据提交到form表单中
        form = UserRegisterForm(data)
        # 验证数据
        # 如果数据通过
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('userpwd')
                                     )
            # 注册后，跳转到登录页面
            return HttpResponseRedirect(reverse('backweb:login'))
        # 数据校验没通过
        else:
            errors = form.errors
            # 将错误信息返回给页面
            return render(request, 'backweb/register.html', {'errors': errors})


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data)
        # 如果表单校验通过
        if form.is_valid():
            # 通过auth匹配数据库中的数据
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('userpwd')
                                     )
            # 如果有该用户，登录
            if user:
                auth.login(request, user)
                # 跳转首页
                return HttpResponseRedirect(reverse('backweb:index'))
            # 否则，重新登录，返回密码错误
            else:
                return render(request, 'backweb/login.html', {'msg': '密码错误'})
        # 如果数据校验没通过,返回校验错误信息
        else:
            return render(request, 'backweb/login.html', {'errors': form.errors})


# 后台首页
@login_required
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'backweb/index.html', {'articles': articles})


# 退出登录
@login_required
def logout(request):
    if request.method == 'GET':
        # auth自带的注销函数
        auth.logout(request)
        # 跳转到登录页面
        return HttpResponseRedirect(reverse('backweb:login'))


# 文章页
@login_required
def article(request):
    if request.method == 'GET':
        # 如果拿不到page，就赋值为1
        page = request.GET.get('page', 1)
        # 获取所有的文章
        articles = Article.objects.filter(is_delete=0)
        # 导入Django的paginator分页包
        paginator = Paginator(articles, 3)
        # 通过自带的page方法获取第一页的内容
        page_articles = paginator.page(page)
        return render(request, 'backweb/article.html', {'page_articles': page_articles, 'articles': articles})


# 删除栏目
def delete_category(request, id):
    if request.method == 'GET':
        category = Category.objects.filter(id=id).first()
        category.is_delete = 1
        category.save()
        return HttpResponseRedirect(reverse('backweb:category'))


# 栏目页
@login_required
def category(request):
    if request.method == 'GET':
        categorys = Category.objects.filter(is_delete=0)
        return render(request, 'backweb/category.html', {'categorys': categorys})

    if request.method == 'POST':
        name = request.POST.get('name')
        describe = request.POST.get('describe')

        Category.objects.create(name=name, describe=describe)
        return HttpResponseRedirect(reverse('backweb:category'))


# 添加文章
def add_article(request):
    if request.method == 'GET':
        categorys = Category.objects.filter(is_delete=0)

        return render(request, 'backweb/add_article.html', {'categorys': categorys})

    if request.method == 'POST':
        title = request.POST.get('title')
        describe = request.POST.get('describe')
        content = request.POST.get('content')
        img = request.FILES.get('img')
        category = Category.objects.filter(name=request.POST.get('category')).first()

        new_article = Article.objects.create(title=title, describe=describe, content=content, img=img, category=category)
        new_article.save()

        return HttpResponseRedirect(reverse('backweb:article'))


# 删除文章
def delete_article(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(id=id).first()
        article.is_delete = 1
        article.save()
        return HttpResponseRedirect(reverse('backweb:article'))


# 修改文章
def edit_article(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(id=id).first()
        categorys = Category.objects.all()
        return render(request, 'backweb/edit_article.html', {'article': article, 'categorys': categorys})

    if request.method == 'POST':
        title = request.POST.get('title')
        describe = request.POST.get('describe')
        content = request.POST.get('content')
        img = request.FILES.get('img')
        category = Category.objects.filter(name=request.POST.get('category')).first()
        new_article = Article.objects.filter(id=id).first()

        new_article.title = title
        new_article.describe = describe
        new_article.content = content
        new_article.img = img
        new_article.category = category
        new_article.save()

        return HttpResponseRedirect(reverse('backweb:article'))

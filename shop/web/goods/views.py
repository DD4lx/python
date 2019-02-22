
from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Goods, GoodsCategory
from utils.functions import login_required


def index(request):
    if request.method == 'GET':
        # user = request.user
        # goods = Goods.objects.all()
        # types = GoodsCategory.CATEGORY_TYPE
        # return render(request, 'web/index.html', {'goods': goods, 'types': types, 'username': user.username})

        goods = Goods.objects.all()
        types = GoodsCategory.CATEGORY_TYPE

        good_type = {}
        for type in types:
            goods_list = []
            count = 0
            for good in goods:
                # 判断商品分类和商品分类
                if count < 4:
                    if type[0] == good.category_id:
                        goods_list.append(good)
                        count += 1
            good_type[type[1]] = goods_list
        return render(request, 'web/index.html', {'good_type': good_type})


def detail(request, id):
    if request.method == 'GET':
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'web/detail.html', {'goods': goods})


def list(request, id):
    if request.method == 'GET':
        goods = Goods.objects.filter(category_id=id)
        type = goods.first().category.CATEGORY_TYPE[int(id)-1][1]
        try:
            page = request.GET.get('page', 1)
        except Exception as e:
            page = 1
        paginator = Paginator(goods, 1)
        page_goods = paginator.page(page)
        return render(request, 'web/list.html', {'goods': goods, 'page_goods': page_goods, 'id': id, 'type': type})



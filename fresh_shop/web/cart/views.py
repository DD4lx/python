from django.http import JsonResponse
from django.shortcuts import render

from cart.models import ShoppingCart
from goods.models import Goods


def add_cart(request):
    if request.method == 'POST':
        # 加入购物车，需要判断用户是否登录
        # 如果登录，加入购物车中的数据，其实就是加入到数据库购物车表中（设计不够好）
        # 如果登录，加入到购物车的数据，存储到session中；（优化登录时的代码，这种设计就相对较好）
        # 如果没登录，加入购物车的数据，是加入到session中的，
        # session中存储数据：只需存商品id，商品数量，商品的选择状态
        # 如果登录了，则把session中数据同步到数据库购物车表中（同步，通过中间件来实现同步数据）

        # 1.获取商品id和商品数量
        goods_id = int(request.POST.get('goods_id'))
        goods_num = int(request.POST.get('goods_num'))
        # 2.组装存到session中的数据格式
        goods_list = [goods_id, goods_num, 1]
        # 在session中存key,value
        # request.session['goods'] = goods_list
        # 存储格式应为：
        # {'goods':[[1,5,1],[2,6,1],...}
        if request.session.get('goods'):
            # 说明session中存储了加入购物车的商品数据
            # 判断当前加入到购物车的数据，是否已经存于session中
            # 如果存在，则修改session中该商品的数量
            # 如果不存在，则新增
            flag = 0
            session_goods = request.session['goods']
            for goods in session_goods:
                # 判断如果加入到购物车中数据，已经存在于session中，则修改
                if goods[0] == goods_id:
                    goods[1] = int(goods[1]) + int(goods_num)
                    flag = 1
            if not flag:
                # 如果不存在，则添加
                session_goods.append(goods_list)
            request.session['goods'] = session_goods
            goods_count = len(session_goods)
            # return JsonResponse({'code': 200, 'msg': '请求成功'})
        else:
            data = []
            data.append(goods_list)
            request.session['goods'] = data
            goods_count = 1
        return JsonResponse({'code': 200, 'msg': '请求成功', 'goods_count': goods_count})


def cart(request):
    if request.method == 'GET':
        # 如果没有登录，则从session中取商品的信息
        # 如果登录，还是从session中取数据（保证数据中的商品和数据库中的商品一致）
        session_goods = request.session.get('goods')

        if session_goods:
            # 获取session中所有的商品id值
            goods_all = []
            for goods in session_goods:

                cart_goods = Goods.objects.filter(pk=goods[0]).first()
                goods_number = goods[1]
                total_price = goods[1] * cart_goods.shop_price
                goods_all.append([cart_goods, goods_number, total_price])
            # 获取商品对象
            # 前台需要商品信息，商品的个数，商品的总价
            # 后台返回结构[[goods objects, goods number, goods price],[goods objects, goods number, goods price]]
            # goods = Goods.objects.filter(pk__in=goods_ids).all()
        else:
            goods_all = ''
        return render(request, 'web/cart.html', {'goods_all': goods_all})


def place_order(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        cart = ShoppingCart.objects.filter(user_id=user_id, is_select=1).all()
        for cart_goods in cart:
            # 给每一个购物车商品对象添加一个total_price属性
            cart_goods.total_price = int(cart_goods.nums) * int(cart_goods.goods.shop_price)
        return render(request, 'web/place_order.html', {'cart': cart})


def cart_count(request):
    if request.method == 'GET':
        # 判断购物车中商品的个数
        user_id = request.session.get('user_id')
        # 当前用户是否登录
        if user_id:
            # 如果用户登录，则返回购物车表中的商品个数
            count = len(ShoppingCart.objects.filter(user_id=user_id))
        else:
            # 如果用户没登录，则返回session中的商品个数
            session_goods = request.session.get('goods')
            count = len(session_goods)
        return JsonResponse({'code': 200, 'msg': '请求成功', 'count': count})


def change_goods_num(request):
    if request.method == 'POST':
        # 修改购物车中商品的个数
        # 1.先判断用户登录与否，如果用户登录没有登录，则修改session中商品的个数
        # 2.如果用户登录，则需要判断当前修改的商品是否存在于session中，
        # 如果存在，则修改session。如果不存在，就修改数据库表中的数据
        # 获取修改的商品的id，商品个数，商品选择状态
        goods_id = request.POST.get('goods_id')
        goods_num = int(request.POST.get('goods_num'))
        is_select = int(request.POST.get('is_select'))

        user_id = request.session.get('user_id')
        # 先判断要修改的商品是否存在于session中，如果存在则修改session中的商品的个数和选择状态
        session_goods = request.session.get('goods')
        if session_goods:
            for goods in session_goods:
                if int(goods_id) == int(goods[0]):
                    goods[1] = goods_num
                    goods[2] = is_select
            request.session['goods'] = session_goods

        # 如果用户登录了，则需要在修改购物车中数据，因为session中的商品有可能并不在购物车表中
        if user_id:
            ShoppingCart.objects.filter(user_id=user_id, goods_id=goods_id).update(nums=goods_num, is_select=is_select)
        return JsonResponse({'code': 200, 'msg': '请求成功'})


def f_price(request):
    """
    返回购物车或session中商品的价格，和总价
    {key:[[id1, price1],[id2, price2]], key2: total_price}
    """
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        if user_id:
            # 获取当前登录系统的用户的购物车中的数据
            carts = ShoppingCart.objects.filter(user_id=user_id)
            cart_data = {}
            cart_data['goods_price'] = [(cart.goods_id, cart.nums * cart.goods.shop_price) for cart in carts]
            all_price = 0
            # 总的价格
            for cart in carts:
                if cart.is_select:
                    all_price += cart.nums * cart.goods.shop_price
                    cart_data['all_price'] = all_price
                    count = int(len(cart_data.get('goods_price')))
        else:
            # 拿到session中所有的商品信息,[id, num, is_select]
            session_goods = request.session.get('goods')
            # 返回数据结构，{’goods_price'：[[id1, price1],[id2, price2]...]}
            cart_data = {}
            data_all = []
            # 计算总价
            all_price = 0
            count = 0
            for goods in session_goods:
                data = []
                data.append(goods[0])
                g = Goods.objects.get(pk=goods[0])
                data.append(int(goods[1]) * g.shop_price)
                # 生成的data为: [id1, price1]
                data_all.append(data)
                # 判断如果商品勾选了，才计算总价格
                if goods[2]:
                    all_price += int(goods[1]) * g.shop_price
                    cart_data['goods_price'] = data_all
                    cart_data['all_price'] = all_price
                    count += 1
                    # count = int(len(cart_data.get('goods_price')))
                # else:
                #     count -= 1
    return JsonResponse({'code': 200, 'cart_data': cart_data, 'count': count})




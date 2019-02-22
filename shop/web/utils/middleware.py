import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from cart.models import ShoppingCart
from user.models import User


class UserAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # TODO:判断某些页面需要登录才能访问，某些页面不需要登录就能访问
        # TODO：需要登录的页面，当用户没有登录时，
        # 屏蔽掉登录和注册的url，不需要做登录验证
        # no_check = ['/user/login/', '/user/register/', '/goods/index/', '/goods/list/(\d+)/', '/goods/detail/(\d+)/']
        # path = request.path
        # if path in no_check:
            # 不需要执行以下登录验证的代码，直接执行视图函数
            # return None
        # else:
            # user_id = request.session.get('user_id')
            # if user_id:
            #     user = User.objects.filter(pk=user_id).first()
            #     request.user = user
            #     return None
            # else:
            #     return HttpResponseRedirect(reverse('user:login'))
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
            # 可以访问所有的页面
            return None

        # 没有登录，既没有user_id
        # 思路：首页，详情页面，登录，注册，访问media不管登录与否都可以查看
        # 下单，结算，订单页面，个人中心页面只能登录才能查看
        no_check_path = ['/user/login/', '/user/register/', '/goods/index/',
                         '/media/(.*)', '/goods/detail/(.*)', '/static/(.*)',
                         '/goods/list/(.*)', '/cart/add_cart/', '/cart/cart/',
                         '/cart/cart_count/', '/cart/f_price/', '/cart/change_goods_num/',
                         '/cart/goods_count/']
        path = request.path
        for no_check in no_check_path:
            # 匹配当前路径是否为不需要登录验证的页面路径
            if re.match(no_check, path):
                return None
        # 当前的请求url不在no_check_path中，则表示当前url需要登录才能访问
        return HttpResponseRedirect(reverse('user:login'))


# 数据库表与session互相同步数据
class SessionSynchronization(MiddlewareMixin):

    def process_request(self, request):
        # session中商品数据和购物车表中数据的同步
        # session中数据结构：[[id, num, is_select]]
        session_goods = request.session.get('goods')
        user_id = request.session.get('user_id')
        if user_id:
            # 用户登录后，才做同步
            if session_goods:
                # 同步：保持session中数据与数据表中数据同步
                # 1.如果session中商品已经存在于数据表中则更新
                # 2.如果session中商品不存在于数据库表中则添加
                # 3.如果session中的商品少于数据表中的商品，则更新session
                for goods in session_goods:
                    # goods的结构[id, num, is_select]
                    cart = ShoppingCart.objects.filter(user_id=user_id, goods_id=goods[0]).first()
                    if cart:
                        # 数据库中能查询到该商品信息
                        cart.nums = goods[1]
                        cart.is_select = goods[2]
                        cart.save()
                    else:
                        # 数据库中查询不到该商品信息，则添加
                        ShoppingCart.objects.create(user_id=user_id,
                                                    goods_id=goods[0],
                                                    nums=goods[1],
                                                    is_select=goods[2])

            # 将数据库数据同步到session中
            carts = ShoppingCart.objects.filter(user_id=user_id).all()
            session_new_goods = [[cart.goods_id, cart.nums, cart.is_select] for cart in carts]
            request.session['goods'] = session_new_goods

            return None


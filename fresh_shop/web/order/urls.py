from django.conf.urls import url

from order import views

urlpatterns = [
    # 下单
    url(r'^order/', views.order, name='order'),
    # 用户订单详细信息
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 付款
    url(r'^pay/(\d+)/', views.pay, name='pay'),
]

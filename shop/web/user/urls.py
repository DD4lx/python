from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),
    # 用户信息
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 用户订单，在订单app中实现
    # url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 用户订单
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),
]


from django.conf.urls import url


from backweb import views


urlpatterns = [
    # 后台首页
    url(r'^index/', views.index, name='index'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 注册
    url(r'^register/', views.register, name='register'),
    # 退出登录，注销
    url(r'^logout/', views.logout, name='logout'),
    # 文章显示
    url(r'^article/', views.article, name='article'),
    # 栏目显示
    url(r'^category/', views.category, name='category'),
    # 增加文章
    url(r'^add_article/', views.add_article, name='add_article'),
    # 删除栏目
    url(r'^delete_category/(\d+)/', views.delete_category, name='delete_category'),
    # 删除文章
    url(r'^delete_article/(\d+)/', views.delete_article, name='delete_article'),
    # 编辑文章
    url(r'^edit_article/(\d+)/', views.edit_article, name='edit_article'),

]


from django.conf.urls import url
from django.contrib.staticfiles.urls import static

from goods import views
from web.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # 首页
    url(r'^index/', views.index, name='index'),
    # 商品详情页
    url(r'^detail/(\d+)/', views.detail, name='detail'),
    # 列表显示
    url(r'^list/(\d+)/', views.list, name='list'),

]
urlpatterns += static(MEDIA_URL,docunment_root=MEDIA_ROOT)

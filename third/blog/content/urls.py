from content import views
from django.conf.urls import url

urlpatterns = [
    url(r'^logout/', views.logout, name='logout'),
    url(r'^index/', views.index, name='index'),
    url(r'^share/', views.share, name='share'),
    url(r'^list/', views.list, name='list'),
    url(r'^about/', views.about, name='about'),
    url(r'gbook/', views.gbook, name='gbook'),
    url(r'info/', views.info, name='info'),
    url(r'infopic/', views.infopic, name='infopic'),
]

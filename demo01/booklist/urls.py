from django.conf.urls import url

from . import views

# 去除硬编码（名称任意，但是需要与命名空间的名称一致，一般取名为项目名称）
app_name = "booklist"
# 去除硬编码 在应用的urlconf中添加url别名(name=)
urlpatterns = [
    # url('index/', views.index),
    # url('index/$', views.index),
    url(r'^$', views.index, name='index'),
    url(r'^booklist/$', views.list, name='list'),
    # url(r'$', views.index),
    url(r'^bookdetail/(\d+)/$', views.detail, name='detail'),
    url(r'^bookinfoss/(\d+)/$', views.infoss, name='infoss'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
]

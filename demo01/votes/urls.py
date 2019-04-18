from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.lists),
    url(r'^ends/(\d+)/$', views.ends),
    url(r'^counts/(\d+)/$', views.counts),
]


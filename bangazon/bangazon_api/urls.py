from django.conf.urls import url, include
from bangazon_api import views

urlpatterns = [
    url(r'^product_list/$', views.product_list),
    url(r'^product_list/(?P<pk>[0-9]+)/$$', views.single_product),
    url(r'^category_list/$', views.category_list),
]
# from django.conf.urls import url
# from bangazon_api import views

# urlpatterns = [
# 	url(r'^orders/$', views.order_list),
# 	url(r'^orders/(?P<pk>[0-9]+)/$', views.order_detail),
# 	url(r'^customers/$', views.list_of_customers, name='list_of_customers'),
# 	url(r'^customers/(?P<customer_id>[0-9]+)/$', views.customer, name='customer'),
# 	url(r'^category_list/$', views.category_list),
# 	url(r'^product_list/$', views.product_list),
# 	url(r'^product_list/(?P<product_id>[0-9]+)/$', views.single_product),
# 	url(r'^payment_types_list/$', views.payment_types_list),
# 	url(r'^payment_types_list/(?P<pk>[0-9]+)/$', views.single_payment_type),
# 	url(r'^productorders/$', views.productorders_list),
#     url(r'^productorders/(?P<pk>[0-9]+)/$', views.productorders_detail),
# ]

from django.conf.urls import url, include
from rest_framework import routers
from bangazon_api import views


router = routers.DefaultRouter()
router.register(r'orders', views.OrdersViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'category', views.CategoriesViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'payment_types', views.PaymentTypesViewSet)
router.register(r'productorders', views.ProductOrdersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


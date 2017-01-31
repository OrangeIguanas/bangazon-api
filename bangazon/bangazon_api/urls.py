from django.conf.urls import url
from bangazon_api import views

urlpatterns = [
	url(r'^orders/$', views.order_list),
	url(r'^orders/(?P<pk>[0-9]+)/$', views.order_detail),
	url(r'^customers/$', views.list_of_customers, name='list_of_customers'),
	url(r'^customers/(?P<customer_id>[0-9]+)/$', views.customer, name='customer'),
	url(r'^category_list/$', views.category_list),
	url(r'^product_list/$', views.product_list),
	url(r'^product_list/(?P<product_id>[0-9]+)/$', views.single_product),
	# url(r'^payment_types_list/$', payment_types_list),
	# url(r'^payment_types_list/(?P<pk>[0-9]+)/$', single_payment_type),
	# url(r'^productorders/$', productorders.site.urls),
]
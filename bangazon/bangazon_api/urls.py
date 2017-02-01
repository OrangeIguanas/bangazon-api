from django.conf.urls import url, include
from rest_framework import routers
from bangazon_api import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrdersViewSet)
router.register(r'customers', views.CustomersViewSet)
router.register(r'category', views.CategoriesViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'payment_types', views.PaymentTypesViewSet)
router.register(r'productorders', views.ProductHasOrdersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.contrib import admin
from . models import Customers, Categories, Products, PaymentType, Orders, ProductHasOrders
# Register your models here.

admin.site.register(Customers)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(PaymentType)
admin.site.register(Orders)
admin.site.register(ProductHasOrders)

from django.contrib import admin
from . models import Customers, Categories, Products
# Register your models here.

admin.site.register(Customers)
admin.site.register(Categories)
admin.site.register(Products)
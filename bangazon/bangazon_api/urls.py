"""Defines URL patterns for bangazon_api app"""

from django.conf.urls import urls
from . import views

#Url patterns for the bangazon_api app
url patterns = [
    #customers
    url(r'^Customers/$', views.list_of_customers, name='list_of_customers')
    url(r'^Customers/(?P<customer_id>[0-9]+)$', views.customer_detail, name='customer_detail')
] 

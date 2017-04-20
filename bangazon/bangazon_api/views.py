from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets


class JSONResponse(HttpResponse):
    """
    author: Ike
    purpose: An HttpResponse that renders its content into JSON.
    Methods: __init__
        purpose: initialize a new instnce of JSON response
        arguments: 
        self- reference to the class instance being created
        data- request data
        kwargs- setting contenty type to application/json
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class CustomersViewSet(viewsets.ModelViewSet):
    """
    purpose: returns the Customers list for the bangazon_api app
    or adds a customer to the customers list
    Author: Ike
    API endpoint that allows users to be viewed or edited.
    queryset: all datatype objects in specified data model
    serializer_class: points to the serializer for data model
    """
    queryset = Customers.objects.all().order_by('last_name')
    serializer_class = CustomersSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    """
    purpose: returns the categories list for the bangazon_api app
    or adds a category to the customers list
    Author: Zach
    API endpoint that allows users to be viewed or edited.
    queryset: all datatype objects in specified data model
    serializer_class: points to the serializer for data model
    """
    queryset = Categories.objects.all().order_by('category_name')
    serializer_class = CategoriesSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    """
    purpose: returns the Customers list for the bangazon_api app
    or adds a customer to the customers list
    Author: Ike
    API endpoint that allows users to be viewed or edited.
    queryset: all datatype objects in specified data model
    serializer_class: points to the serializer for data model
    """
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializer

class PaymentTypesViewSet(viewsets.ModelViewSet):
    """
    author: Pete
    purpose: Returns the payment type list for bangazon_api app
    or adds a payment to the list
    queryset: all datatype objects in specified data model
    serializer_class: points to the serializer for data model
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypesSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    """
    purpose: returns the orders list for the bangazon_api app
    or adds an order to the list. This is API endpoint that allows
    users to be viewed or edited.
    Author: Pete
    queryset: all datatype objects in specified data model
    serializer_class: points to the serializer for data model
    """
    queryset = Orders.objects.all()
    serializer_class = CategoriesSerializer


class ProductHasOrdersViewSet(viewsets.ModelViewSet):
    """
    purpose: returns the Customers list for the bangazon_api app
    or adds a customer to the customers list
    Author: Shawn
    API endpoint that allows users to be viewed or edited.
    queryset: all datatype objects in specified data model
    serializer_class: points to the serializer for data model
    """
    queryset =  ProductHasOrders.objects.all()
    serializer_class = ProductHasOrdersSerializer


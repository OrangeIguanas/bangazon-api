from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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

class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class ProductOrdersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ProductHasOrders.objects.all()
    serializer_class = ProductHasOrdersSerializer

class PaymentTypesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypesSerializer












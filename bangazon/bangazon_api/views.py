from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bangazon_api.models import *
from bangazon_api.serializers import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def product_list(request):
    """
    Retrieve, update or delete a product.
    """
    try:
        product_list = Products.objects.all(request)# Returns All product objects
    except Products.DoesNotExist: #Handle Any Exceptions
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductsSerializer(product_list, many=True) #When getting many objects include many=True as a parameter
        return JSONResponse(serializer.data)# Returning Data as Json

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(product_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product_list.delete()
        return HttpResponse(status=204)


def single_product(request, product_id):
    '''
    Retrieve, update or delete a single product.

    '''

    try: 
        single_product = Products.objects.get(id = product_id)#Returns Products with A specific Id
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductsSerializer(product_id)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(single_product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONRenderer(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        single_product.delete()
        return HttpResponse(status=204)

def category_list(request):

    try:
        category = Categories.object.all(request)
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategoriesSerializer(category, many=True)
        return JSONResponse(serializaer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONRenderer(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)

        
def list_of_customers(request):
    """
    purpose: returns the Customers list for the bangazon_api app
    or adds a customer to the customers list
    

    """
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return JSONResponse(serializer.data)

    elif request.method = 'POST':
        data = JSONParser().parse(request)
        serializer = CustomersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    # context =  {'customers' : customers} # a context is a dictionary in which
    # #keys are names we'll use in the template to access the data and values are 
    # #the data we need to send to the template

# @csrf decorator (@) to denote that this function should be
# run despite not having a CSRF token, which is is the cross-site request
 # forgery defense system

 

def customer(request, customer_id):
    """
    purpose: Show a single customer and customer details
    arguments:
        request- request object that extends HttpRequest, the request
        represents an incoming HTTP request, including user-submitted data
        and HTTP headers
        customer_id- the unique ID for the given customer
    """
    #try to retrieve customer object that matches our customer id, if that
    # customer does not exist then display 404 error
    try:
        customer = Customers.objects.get(id=customer_id)
    except Customers.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CustomersSerializer(customer)
        return JSONResponse(serializer.data)

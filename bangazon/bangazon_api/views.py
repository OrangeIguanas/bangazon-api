from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


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


@csrf_exempt
def product_list(request):
    """
    author: Ike
    purpose: Show a list of products
    arguments:
    request- request object that extends HttpRequest, the request
    represents an incoming HTTP request, including user-submitted data
    and HTTP headers
    
    """
    #try to retrieve product_list object if that
    # list does not exist then display 404 error
    try:
        product_list = Products.objects.all()# Returns All product objects
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

@csrf_exempt
def single_product(request, product_id):
    """
    author: Zach
    purpose: Show a single product and product details
    arguments:
    request- request object that extends HttpRequest, the request
    represents an incoming HTTP request, including user-submitted data
    and HTTP headers
    product_id - the unique ID for the given product
    """
    #try to retrieve product object that matches our product id, if that
    # single_product does not exist then display 404 error

    try: 
        single_product = Products.objects.get(id = product_id)#Returns Products with A specific Id
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductsSerializer(single_product)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(single_product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        single_product.delete()
        return HttpResponse(status=204)

@csrf_exempt
def category_list(request):
    """
    author: Zach
    purpose: returns the Categories list for the bangazon_api app
    or adds a Category to the Categories list
    arguments:
    request- request object that extends HttpRequest, the request
    represents an incoming HTTP request, including user-submitted data
    and HTTP headers

    """
    #try to retrieve category object that matches our category id, if that
    # category does not exist then display 404 error


    try:
        category = Categories.objects.all()
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategoriesSerializer(category, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)

@csrf_exempt       
def list_of_customers(request):
    """
    author: Ike
    purpose: returns the Customers list for the bangazon_api app
    or adds a customer to the customers list
    arguments:
        request- request object that extends HttpRequest, the request
        represents an incoming HTTP request, including user-submitted data
        and HTTP headers
    """

    if request.method == 'GET':
        customers = Customers.objects.all() #gets all customer objects
        serializer = CustomersSerializer(customers, many=True)
        return JSONResponse(serializer.data)

    #Add customer to customer list (if request method is post)
    elif request.method == 'POST':
        #converts python data types into json
        data = JSONParser().parse(request)
        serializer = CustomersSerializer(data=data)
        
        #save customer to database if data structure is correct
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
      
    #a context is a dictionary in which
    #keys are names we'll use in the template to access the data and values are 
    #the data we need to send to the template
    context =  {'customers' : customers} 
    

 # @csrf decorator (@) to denote that this function should be
 # run despite not having a CSRF token, which is is the cross-site request
 # forgery defense system

 
@csrf_exempt
def customer(request, customer_id):
    """
    author: Ike
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
        # pass the customer object into the Serializer which will convert model
        # data to python data type
        serializer = CustomersSerializer(customer)
        #convert data type to JSONResponse
        return JSONResponse(serializer.data)



@csrf_exempt
def order_list(request):
    """
    author: Abby
    purpose: Allow user to get("view") and post("create") data
    arguments: request - Request extends Django's HttpRequest
    
    """
    if request.method == 'GET':
        order = Orders.objects.all()
        serializer = OrdersSerializer(order, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrdersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201) #201 - Request Fulfilled
        return JSONResponse(serializer.errors, status=400) #400 - Bad Request




@csrf_exempt
def order_detail(request, pk):
    """
    author: Abby
    purpose: Allow user to get("view") and put("update") and delete data
    arguments: request - Request extends Django's HttpRequest, pk - Primary Key
    
    """

    try:
        order = Orders.objects.get(pk=pk)
    except Orders.DoesNotExist:
        return HttpResponse(status=404) #404 - Not found

    if request.method == 'GET':
        serializer = OrdersSerializer(order)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrdersSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400) #400 - Bad Request

    elif request.method == 'DELETE':
        order.delete()
        return HttpResponse(status=204) #204 - Fulfilled - No Additional Content

@csrf_exempt
def payment_types_list(request):
    """
    author: Pete
    purpose: Show a list of products
    arguments:
    request- request object that extends HttpRequest, the request
    represents an incoming HTTP request, including user-submitted data
    and HTTP headers
    
    """
    #try to retrieve product_list object if that
    # list does not exist then display 404 error
    try:
        payment_types_list = PaymentType.objects.all()# Returns All product objects
    except PaymentType.DoesNotExist: #Handle Any Exceptions
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PaymentTypesSerializer(payment_types_list, many=True) #When getting many objects include many=True as a parameter
        return JSONResponse(serializer.data)# Returning Data as Json

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaymentTypesSerializer(payment_types_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        payment_types_list.delete()
        return HttpResponse(status=204)


def single_payment_type(request, pk):
    """
    author: Pete
    purpose: Show a single product and product details
    arguments:
    request- request object that extends HttpRequest, the request
    represents an incoming HTTP request, including user-submitted data
    and HTTP headers
    product_id - the unique ID for the given product
    """
    #try to retrieve product object that matches our product id, if that
    # single_product does not exist then display 404 error

    try: 
        single_payment_type = PaymentType.objects.get(pk=pk)#Returns Products with A specific Id
    except PaymentType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PaymentTypesSerializer(single_payment_type)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaymentTypesSerializer(single_payment_type, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        single_product.delete()
        return HttpResponse(status=204)





@csrf_exempt
def productorders_list(request):


    """
    purpose: Allow user to get("view") and post("create") data
    arguments: request - Request extends Django's HttpRequest
    author: Shawn
    """
    try:
        productorders_list = ProductHasOrders.objects.all()# Returns All product objects
    except ProductHasOrders.DoesNotExist: #Handle Any Exceptions
        return HttpResponse(status=404)


    if request.method == 'GET':
        product = ProductHasOrders.objects.all()
        serializer = ProductHasOrdersSerializer(product, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ProductHasOrdersSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)




@csrf_exempt
def productorders_detail(request, pk):

    """
    purpose: Allow user to get("view") and put("update") and delete data
    arguments: request - Request extends Django's HttpRequest,pk - Primary Key
    author: Shawn
    """


    try:
        single_productorders = ProductHasOrders.objects.get(pk=pk)
    except ProductHasOrders.DoesNotExist:
        return HttpResponse(status=404) #not found error

    if request.method =='GET':
        serializer = ProductHasOrdersSerializer(single_productorders)
        return JSONResponse(serializer.data)

    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = ProductHasOrdersSerializer(single_productorders, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        single_productorders.delete()
        orders.delete()
        return HttpResponse(status=204) #fulfilled request 


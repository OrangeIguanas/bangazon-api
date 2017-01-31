from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Customers
from .serializers import CustomersSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.

@csrf_exempt
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
@csrf_exempt 
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
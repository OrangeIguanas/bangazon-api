from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

class JSONResponse(HttpResponse):
	"""
	purpose: An HttpResponse that renders its content into JSON.
	Author: Ike
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

# Create your views here.

@csrf_exempt
def list_of_customers(request):
	"""
	purpose: returns the Customers list for the bangazon_api app
	or adds a customer to the customers list
	Author: Ike
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
	context =  {'Customers' : Customers} 
	

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
		# pass the customer object into the Serializer which will convert model
		# data to python data type
		serializer = CustomersSerializer(customer)
		#convert data type to JSONResponse
		return JSONResponse(serializer.data)



@csrf_exempt
def order_list(request):
	"""
	purpose: Allow user to get("view") and post("create") data
	arguments: request - Request extends Django's HttpRequest
	author: Abby
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
	purpose: Allow user to get("view") and put("update") and delete data
	arguments: request - Request extends Django's HttpRequest, pk - Primary Key
	author: Abby
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



from rest_framework import serializers
from bangazon_api.models import *


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    """
    purpose: convert complex data
    into native python datatypes for JSON
    rendering
    author: Ike
    methods and subclasses: meta
        model: Customers from models.py
        fields: all fields form Customers data model are included
    """
    #Use of hyperlink serializer requires context to be a parameter when instantiating
    class Meta:
        model = Customers
        fields = ('first_name', 'last_name', 'created_date', 'street_address',
         'city', 'zip_code', 'state')


class ProductsSerializer(serializers.ModelSerializer):
    """ 
    ProductsSerializer class
    The purpose of this class is to convert the Products data model to Json.
    author: Zach
    subclasses: Meta (contains fields that are to be converted)
    
    """
    class Meta:
        model = Products
        fields = ('name', 'price', 'description', 'quantity', 'category_Id', 'customer_Id')

class CategoriesSerializer(serializers.ModelSerializer):
    """ 
    CategoriesSerializer class
    The purpose of this class is to convert the Categories data model to Json.
    author: Zach
    subclasses: Meta (contains fields that are to be converted)
    
    """

    class Meta:
        model = Categories
        fields = ('category_name',)

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
	""" purpose: convert model to JSON format
		author: Pete
		methods: Meta
		Class: Orders
		Fields: Include all 
	"""
	class Meta:
		model = Orders
		fields = ('payment_types_id',)


class PaymentTypesSerializer(serializers.ModelSerializer):
	""" purpose: convert PaymentTypes model to JSON format
		author: Abby
		methods: Meta
		Class: PaymentTypes
		Fields: Include all
	"""
	class Meta:
		model = PaymentType
		fields = ('card_type', 'card_number', 'cvv', 'expiration', 'billing_name', 'customer_id' )


class ProductHasOrdersSerializer(serializers.ModelSerializer):
	""" purpose: convert ProductHasOrders model to JSON format
		author: Shawn
		methods: Meta
		Class: ProductHasOrders
		Fields: Include all
	"""
	class Meta: 
		model = ProductHasOrders
		fields = ('product','orders')

from rest_framework import serializers
from bangazon_api.models import *


class ProductsSerializer(serializers.ModelSerializer):

	"""
	ProductsSerializer class
	The purpose of this class is to convert the Products data model to Json.
	author: Zach
	subclasses: Meta (contains fields that are to be converted)

	"""
	class Meta:
		model = Products
		fields = (
			'name', 'price', 'description', 'quantity', 'category', 'customer')


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

	''' purpose: convert model to JSON format
			author: Pete
			methods: Meta
			Class: Orders
			Fields: Include all
	'''
	class Meta:
		model = Orders
		fields = ('payment_types',)


class ProductHasOrdersSerializer(serializers.HyperlinkedModelSerializer):

	''' purpose: convert model to JSON format
		author: Shawn
		methods: Meta
		Class: ProductHasOrder
		Fields: Include all
	'''
	class Meta:
		model = ProductHasOrders
		fields = ('product', 'orders',)
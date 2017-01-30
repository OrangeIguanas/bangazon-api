from rest_framework import serializers
from bangazon_api.models import *


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
	''' purpose: convert model to JSON format
		author: Pete
		methods: Meta
		Class: Orders
		Fields: Include all 
	'''
	class Meta:
		model = Orders
		fields = ('payment_types_id',)
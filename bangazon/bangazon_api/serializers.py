from rest_framework import serializers
from bangazon_api.models import *

# Create a Serializer for the Order class to convert it to JSON format. 
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('payment_types_id',)
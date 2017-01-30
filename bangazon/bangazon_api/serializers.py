from rest_framework import serializers
from bangazon_api.models import Products
from bangazon_api.models import Categories

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'price', 'description', 'quantity', 'category_Id', 'customer_Id')

class CategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categories
		fields = ('category_name',)


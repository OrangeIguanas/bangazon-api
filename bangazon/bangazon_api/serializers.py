from rest_framework import serializers
from bangazon_api.models import Products
from bangazon_api.models import Categories

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


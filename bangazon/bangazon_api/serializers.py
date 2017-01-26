from rest_framework import serializers

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
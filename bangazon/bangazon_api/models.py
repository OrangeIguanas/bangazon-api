from django.db import models

# purpose: this class is to create a junction table between 
# the product table and the order table .
# author: Shawn 
# method: none 

class product_order (models.Model):
	product_id = models.Foreignkey("product_id", related_name = 'product_id')
	order_id = models.Foreignkey("order_id", related_name = 'order_id')



class Customers(models.Model):
    """Customers model class
        The purpose of this class is to define the Customers data model.
        author: Ike
        methods: none
        subclasses: Meta (with ordering by last_name)
    """
    
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length =50)
    created_date = models.DateTimeField(auto_now_add=True)
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=35)

    class Meta:
        ordering = ('last_name',)


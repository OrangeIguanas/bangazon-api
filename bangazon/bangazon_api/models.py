from django.db import models

# purpose: this class is to create a junction table between 
# the product table and the order table .
# author: Shawn 
# method: none 

class product_order (models.Model):
	product_id = models.Foreignkey("product_id", related_name = 'product_id')
	order_id = models.Foreignkey("order_id", related_name = 'order_id')


from django.db import models

# Create your models here.
class product_has_order (models.Model):
	product_id = models.Integerfield
	order_id = models.Integerfield

class Meta: 
	ordering = (product_id, order_id)

	
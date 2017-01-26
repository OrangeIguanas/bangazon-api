from django.db import models

# Create your models here.



class PaymentType(models.Model):
	"""PaymentType model class
	    The purpose of this class is to define customer's payment types
	    author: Abby
	    methods: none
	    meta: plural name
	"""
	card_type = models.CharField(max_length=30)
	card_number = models.CharField(max_length=25)
	cvv = models.CharField(max_length=4)
	expiration = models.DateField(auto_now=False)
	billing_name = models.CharField(max_length=55)
	customer_id = models.ForeignKey(Customer)

	class Meta:
		verbose_name_plural = "PaymentTypes"


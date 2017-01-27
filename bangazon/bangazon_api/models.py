from django.db import models

# Create your models here.

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


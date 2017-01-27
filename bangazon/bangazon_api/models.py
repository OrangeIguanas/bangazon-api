from django.db import models

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

class Categories(models.Model):
    """ 
    Categories model class
    The purpose of this class is to define the Categories data model.
    author: Zach
    subclasses: Meta (with ordering by name)
    
    """
    name= models.CharField(max_length=55)

    class Meta:
        ordering = ('name',)


class Products(models.Model):

    """ 
    Products model class
    The purpose of this class is to define the Product data model.
    author: Zach
    subclasses: Meta (with ordering by name)
    DecimalField(max_digits=6, decimal_places=2) ex. 9999.99
    max_digits in decimal field is the total number of digits including the decimal places.
    
    """
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=140)
    quantity = models.IntegerField()
    category_Id = models.ForeignKey(Categories)
    customer_Id = models.ForeignKey(Customers)

    class Meta:
        ordering = ('name',)




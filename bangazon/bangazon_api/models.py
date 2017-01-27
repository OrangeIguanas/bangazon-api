from django.db import models




class Customers(models.Model):
    """Customers model class
        The purpose of this class is to define the Customers data model.
        author: Ike
        methods: __str__ Returns a string
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

<<<<<<< HEAD
=======
    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.first_name, self.last_name, self.created_date, self.street_address, self.city, self.zip_code, self.state)

class Categories(models.Model):
    """ 
    Categories model class
    The purpose of this class is to define the Categories data model.
    author: Zach
    subclasses: Meta (with ordering by name)
    
    """
    category_name = models.CharField(max_length=55)

    class Meta:
        ordering = ('category_name',)

    def __str__(self):
        return '{}'.format(self.name)

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
    category_Id = models.ForeignKey(Categories, null=True)
    customer_Id = models.ForeignKey(Customers, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.name, self.price, self.description, self.quantity, self.category_Id, self.customer_Id)

    """
    purpose: this class is to create a junction table between 
    the product table and the order table .
    author: Shawn 
    method: none 
    
    """

class product_order (models.Model):
    product_id = models.Foreignkey("product_id", related_name = 'product_id')
    order_id = models.Foreignkey("order_id", related_name = 'order_id')

    class Meta:

    def __str__(self):
        return '{} {}'.format(self.product_id, self.order_id)

        
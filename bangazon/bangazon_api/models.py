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


class PaymentType(models.Model):
    """PaymentType model class
        The purpose of this class is to define customer's payment types
        author: Abby
        methods: string return
        meta: plural name
    """
    card_type = models.CharField(max_length=30)
    card_number = models.CharField(max_length=25)
    cvv = models.CharField(max_length=4)
    expiration = models.DateField(auto_now=False)
    billing_name = models.CharField(max_length=55)
    customer_id = models.ForeignKey(Customers, null=True)

    class Meta:
        verbose_name_plural = "PaymentTypes"

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.card_type, self.card_number, self.cvv, self.expiration, self.billing_name, self.customer_id,)


class Orders(models.Model): 
    """Order Class
        This class tracks individual customer orders
        author: Peter
        Methods: returns foreign key of Payment Type as int
    """
    payment_types_id = models.ForeignKey(PaymentType, null=True)
   
    def __int__(self):
        return '{}'.format(self.payment_types_id)


from django.db import models


class Products(models.Model):

""" Products model class
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
    categoryId = models.ForeignKey(Category)
    customerId = models.ForeignKey(Customer)

    class Meta:
        ordering = ('name',)


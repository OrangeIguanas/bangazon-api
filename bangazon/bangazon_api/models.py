from django.db import models

"""Customers model class
    The purpose of this class is to define the Customers data model.
    author: Ike
    methods: none
    subclasses: Meta (with ordering by last_name)

"""
class Customers(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length =100)
    created_date = models.DateTimeField(auto_now_add=True)
    street_address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=20)

    class Meta:
        ordering = ('last_name',)
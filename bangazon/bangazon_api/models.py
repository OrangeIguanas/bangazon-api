from django.db import models

"""Customers model class
    The purpose of this class is to define the Customers data model.
    author: Ike
    methods: none
    subclasses: Meta (with ordering by last_name)

"""
class Customers(models.Model):
    first_name = CharField(max_length=100, default='')
    last_name = CharField(max_length =100)
    created_date = DateTimeField(auto_now_add=True)
    street_address = TextField()
    city = CharField(max_length=100)
    zip_code = IntegerField(max_length=12)
    state = CharField(max_length=20)

    class Meta:
        ordering = ('last_name',)
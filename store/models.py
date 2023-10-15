from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True) # email field

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    # image = models.ImageField()

# class Cart(models.Model):
    # customer 
    # total_price

# class CartItem(models.Model):
    # product 
    # quantity 

# class Order(models.Model):
    # customer 
    # date_ordered 
    # transaction_id

# class OrderItem(models.Model):
    # product 
    # quantity 
    # order 
    # date_added 

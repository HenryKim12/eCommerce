from django.db import models

# Create your models here.
class Address(models.Model):
    unit_number = models.IntegerField()
    address_line = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

class User(models.Model):
    email_address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=64)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Category(models.Model):
    parent_category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    category_name = models.CharField(max_length=64)

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    product_image = models.CharField(max_length=512)

class Promotion(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    discount_rate = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

class Promotion_Category(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart_Item(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Payment_Method(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=64)
    account_number = models.IntegerField()
    expiry_date = models.DateField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    payment_method = models.ForeignKey(Payment_Method, on_delete=models.CASCADE)


from datetime import timezone
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default="Common")  # Added ForeignKey
    description = models.TextField()
    imageUrl = models.URLField()

    def __str__(self):
        return self.name
class Customer(models.Model):
    customer_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    ADDRESS_TYPES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    ]

    customer = models.ForeignKey('Customer', related_name='addresses', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPES)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    contact_number=models.CharField(max_length=10)


class Login(models.Model):
    customer_id = models.CharField(max_length=255)  # Assuming it can be either mobile or email
    password = models.CharField(max_length=255)


from .models import Customer

class OrderedItems(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE , default="9999999999")
    quantity = models.IntegerField()    
    def __str__(self):
        return self.name  

class ConfirmOrder(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_id = models.ForeignKey(OrderedItems, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Order {self.pk} - {self.customer}"


from django.db import models


from django.db import models

class BillDetails(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_items = models.ManyToManyField('OrderedItems', related_name='bills', blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BillDetails {self.pk}"

  










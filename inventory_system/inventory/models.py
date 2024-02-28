from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='inventory/images/')
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    items = models.ManyToManyField(Item)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Order: {self.id}'
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'Order: {self.order.id}, Item: {self.item.name}, Quantity: {self.quantity}'
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    items = models.ManyToManyField(Item)
    
    def __str__(self):
        return self.name
    
    
class InventoryTransaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Item: {self.item.name}, Quantity: {self.quantity}, Type: {self.transaction_type}'
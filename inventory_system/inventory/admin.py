from django.contrib import admin
from .models import Item, Category, Order, OrderItem, Supplier
# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Supplier)



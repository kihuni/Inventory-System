from django.contrib import admin
from .models import Item, Category, Order, OrderItem, Supplier

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Supplier)


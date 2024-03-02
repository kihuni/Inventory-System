from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Category, Order, Supplier
from django.urls import reverse_lazy

# Create your views here.
class ProductListView(ListView):
    model = Item
    template_name = 'product_list.html'
    
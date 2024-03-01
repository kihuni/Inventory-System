from django.urls import path
from . import views

urlpatterns = [
    path('Item/', views.ItemList.as_view(), name='item_list'),
    path('Item/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('Item/Create/', views.ItemCreate.as_view(), name='item_create'),
    path('Item/Update/<int:pk>/', views.ItemUpdate.as_view(), name='item_update'),
    path('Item/Delete/<int:pk>/', views.ItemDelete.as_view(), name='item_delete'),
    
    path('Category/', views.CategoryList.as_view(), name='category_list'),
    path('Category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('Category/Create/', views.CategoryCreate.as_view(), name='category_create'),
    path('Category/Update/<int:pk>/', views.CategoryUpdate.as_view(), name='category_update'),
    path('Category/Delete/<int:pk>/', views.CategoryDelete.as_view(), name='category_delete'),
    
    path('Order/', views.OrderList.as_view(), name='order_list'),
    path('Order/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('Order/Create/', views.OrderCreate.as_view(), name='order_create'),
    path('Order/Update/<int:pk>/', views.OrderUpdate.as_view(), name='order_update'),
    path('Order/Delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
    
    path('Supplier/', views.SupplierList.as_view(), name='supplier_list'),
    path('Supplier/<int:pk>/', views.SupplierDetail.as_view(), name='supplier_detail'),
    path('Supplier/Create/', views.SupplierCreate.as_view(), name='supplier_create'),
    path('Supplier/Update/<int:pk>/', views.SupplierUpdate.as_view(), name='supplier_update'),
    path('Supplier/Delete/<int:pk>/', views.SupplierDelete.as_view(), name='supplier_delete'),
    
   
]
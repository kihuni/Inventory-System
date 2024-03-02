from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, SupplierViewSet, InventoryTransactionViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'inventory_transactions', InventoryTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

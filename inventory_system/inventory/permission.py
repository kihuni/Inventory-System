from rest_framework import permissions


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()
    
class IsProcurement(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Procurement').exists()
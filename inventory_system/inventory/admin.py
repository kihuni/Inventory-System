from django.contrib import admin
from django.contrib.auth.models import Group, Permission, User
from .models import Item, Category, Order, OrderItem, Supplier

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Supplier)


def create_groups():
    # Define permissions
    manager_permissions = [
        ('can_view_inventory', 'Can view inventory'),
        ('can_add_inventory', 'Can add inventory'),
        ('can_change_inventory', 'Can change inventory'),
        ('can_delete_inventory', 'Can delete inventory'),
        ('can_view_orders', 'Can view orders'),
        ('can_add_orders', 'Can add orders'),
        ('can_change_orders', 'Can change orders'),
        ('can_delete_orders', 'Can delete orders'),
        ('can_view_suppliers', 'Can view suppliers'),
        ('can_add_suppliers', 'Can add suppliers'),
        ('can_change_suppliers', 'Can change suppliers'),
        ('can_delete_suppliers', 'Can delete suppliers'),
    ]

    procument_permissions = [
        ('can_view_inventory', 'Can view inventory'),
        ('can_view_orders', 'Can view orders'),
        ('can_add_orders', 'Can add orders'),
        ('can_change_orders', 'Can change orders'),
        ('can_delete_orders', 'Can delete orders'),
        ('can_view_suppliers', 'Can view suppliers'),
        ('can_add_suppliers', 'Can add suppliers'),
        ('can_change_suppliers', 'Can change suppliers'),
        ('can_delete_suppliers', 'Can delete suppliers'),
    ]

    # Create groups
    manager_group, _ = Group.objects.get_or_create(name='Manager')
    procurement_group, _ = Group.objects.get_or_create(name='Procurement')
    
    # Assign permissions to groups
    for codename, name in manager_permissions:
        permission = Permission.objects.get(codename=codename)
        manager_group.permissions.add(permission)

    for codename, name in  procument_permissions:
        permission = Permission.objects.get(codename=codename)
        procurement_group.permissions.add(permission)


def assign_user_to_group(username, group_name):
    try:
        user = User.objects.get(username=username)
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        print(f"User '{username}' added to group '{group_name}' successfully.")
    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")
    except Group.DoesNotExist:
        print(f"Group '{group_name}' does not exist.")


# Call functions
create_groups()
assign_user_to_group('Managers', 'Manager')

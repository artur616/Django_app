from django.shortcuts import render
from .models import MenuItem

def display_menu(request, menu_name=None):
    if menu_name is None:
        menu_items = MenuItem.objects.filter(parent=None).prefetch_related('children')
    else:
        menu_items = MenuItem.objects.filter(title=menu_name).prefetch_related('children')
    return render(request, 'menu/menu.html', {'menu_items': menu_items})

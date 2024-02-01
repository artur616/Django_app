from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).prefetch_related('children')
    return {'menu_items': menu_items}

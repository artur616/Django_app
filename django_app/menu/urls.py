# menu/urls.py
from django.urls import path
from .views import display_menu

urlpatterns = [
    path('<str:menu_name>/', display_menu, name='display_menu'),
    path('', display_menu, name='default_menu'),  # Добавляем путь для отображения меню по умолчанию
]

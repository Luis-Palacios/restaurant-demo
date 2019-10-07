from django.shortcuts import render
from .models import MenuItem
from config.models import GeneralInfo

def index(request):
    general_info = GeneralInfo.objects.first()
    menu_items = MenuItem.objects.order_by('-category__name', 'order').filter(active=True)
    return render(request, 'menu/menu.html', {
        'general_info': general_info,
        'menu_items': menu_items
    })

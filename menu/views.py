from django.shortcuts import render
from .models import MenuCategory, MenuTag
from config.models import GeneralInfo

def index(request):
    general_info = GeneralInfo.objects.first()
    menu_categories = MenuCategory.objects.order_by('order').filter(active=True)
    menu_tags = MenuTag.objects.all()
    return render(request, 'menu/menu.html', {
        'general_info': general_info,
        'menu_categories': menu_categories,
        'menu_tags': menu_tags
    })

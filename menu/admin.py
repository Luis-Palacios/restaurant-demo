from django.contrib import admin
from django.utils.html import format_html
from .models import MenuCategory

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'image_tag', 'active']
    list_editable = ['order', ]
    ordering = ['order', ]
    list_filter = ['active']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:150px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

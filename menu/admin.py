from django import forms
from django.contrib import admin
from django.utils.html import format_html
from ckeditor.widgets import CKEditorWidget
from .models import MenuCategory, MenuItem, MenuTag


class MenuItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = MenuItem
        fields = '__all__'


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'image_tag', 'active']
    list_editable = ['order', ]
    ordering = ['order', ]
    list_filter = ['active']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:150px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

@admin.register(MenuTag)
class MenuTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'icon_tag']

    def icon_tag(self, obj):
        return format_html('<i class="{}" />'.format(obj.icon))

    class Media:
        js = ('https://kit.fontawesome.com/6274f95d8c.js', )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemAdminForm
    list_display = ['name', 'category', 'order', 'tags_icons', 'image_tag', 'price', 'active']
    list_editable = ['order', ]
    ordering = ['category__order',  'order', ]
    list_filter = ['active', 'category', 'tags']
    filter_horizontal = ['tags']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:150px" />'.format(obj.image.url))

    def tags_icons(self, obj):
        tags = obj.tags.all()
        icons = ''
        for tag in tags:
            icons += ' <i class="{}" title="{}"></i>'.format(tag.icon, tag.name)
        return format_html(icons)

    class Media:
        js = ('https://kit.fontawesome.com/6274f95d8c.js', )

    image_tag.short_description = 'Image'
    tags_icons.short_description = 'Tags'
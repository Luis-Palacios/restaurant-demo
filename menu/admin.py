from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.forms.widgets import TextInput
from ckeditor.widgets import CKEditorWidget
from .models import MenuCategory, MenuItem, MenuTag


class MenuItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuTagAdminForm(forms.ModelForm):
    class Meta:
        model = MenuTag
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'image_tag', 'active']
    list_editable = ['order', ]
    ordering = ['order', ]
    list_filter = ['active']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:85px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

@admin.register(MenuTag)
class MenuTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'icon_tag']
    form = MenuTagAdminForm

    def icon_tag(self, obj):
        return format_html('<i class="{}" style="color:{}" />'.format(obj.icon, obj.color))

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
    search_fields = ['name', 'category__name', 'tags__name']
    list_per_page = 10

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:100px" />'.format(obj.image.url))

    def tags_icons(self, obj):
        tags = obj.tags.all()
        icons = ''
        for tag in tags:
            icons += ' <i class="{}" title="{}" style="color:{}"></i>'.format(tag.icon, tag.name, tag.color)
        return format_html(icons)

    class Media:
        js = ('https://kit.fontawesome.com/6274f95d8c.js', )

    image_tag.short_description = 'Image'
    tags_icons.short_description = 'Tags'
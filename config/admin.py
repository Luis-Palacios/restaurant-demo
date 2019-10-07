from django.contrib import admin
from .models import GeneralInfo


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


    def has_add_permission(self, request):
        return GeneralInfo.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        return False

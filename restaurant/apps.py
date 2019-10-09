from django.contrib.admin.apps import AdminConfig

class RestaurantAdminConfig(AdminConfig):
    default_site = 'restaurant.admin.RestaurantAdmin'
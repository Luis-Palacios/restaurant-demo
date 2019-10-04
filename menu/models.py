from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField()
    image = models.ImageField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


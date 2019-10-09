from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField()
    image = models.ImageField(upload_to='categories/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MenuTag(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=50,
                            help_text='<a href="https://fontawesome.com/icons?d=gallery&m=free" target="_blank">Check available icons</a>')
    color = models.CharField(max_length=7)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField()
    image = models.ImageField(upload_to='items/')
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(MenuCategory,
                                 on_delete=models.CASCADE,
                                 limit_choices_to={'active': True},)
    tags = models.ManyToManyField(MenuTag, limit_choices_to={'active': True}, blank=True)

    def __str__(self):
        return self.name

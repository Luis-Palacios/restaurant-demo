from django.db import models

class GeneralInfo(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    logo = models.ImageField(upload_to='info/')

    class Meta:
        verbose_name_plural = 'General Information'

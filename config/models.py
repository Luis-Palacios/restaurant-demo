from django.db import models

class GeneralInfo(models.Model):
    name = models.CharField(max_length=250)
    telephone = models.CharField(max_length=12)
    address = models.TextField()
    logo = models.ImageField(upload_to='info/')

    class Meta:
        verbose_name_plural = 'General Information'

# Generated by Django 2.2.6 on 2019-10-04 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20191004_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menutag',
            old_name='icons',
            new_name='icon',
        ),
    ]
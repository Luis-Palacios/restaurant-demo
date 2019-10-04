# Generated by Django 2.2.6 on 2019-10-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('logo', models.ImageField(upload_to='info/')),
            ],
        ),
    ]

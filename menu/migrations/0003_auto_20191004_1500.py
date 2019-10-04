# Generated by Django 2.2.6 on 2019-10-04 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menucategory_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='image',
            field=models.ImageField(upload_to='categories/'),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('order', models.IntegerField()),
                ('image', models.ImageField(upload_to='items/')),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MenuCategory')),
            ],
        ),
    ]

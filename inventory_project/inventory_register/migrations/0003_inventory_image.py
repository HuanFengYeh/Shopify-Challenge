# Generated by Django 4.0.1 on 2022-01-09 23:14

from django.db import migrations, models
import inventory_register.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_register', '0002_inventory_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='image',
            field=models.ImageField(null=True, upload_to=inventory_register.models.inventory_image_file_path),
        ),
    ]

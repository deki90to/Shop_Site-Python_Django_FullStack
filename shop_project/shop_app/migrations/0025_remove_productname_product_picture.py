# Generated by Django 3.1.2 on 2021-01-16 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0024_auto_20210116_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productname',
            name='product_picture',
        ),
    ]
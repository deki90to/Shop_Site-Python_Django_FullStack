# Generated by Django 3.1.2 on 2021-02-16 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0018_auto_20210215_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='buyed_item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyed_item', to='shop_app.productname'),
        ),
    ]

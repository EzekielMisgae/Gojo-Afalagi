# Generated by Django 4.1.5 on 2023-01-10 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_product_customer_fullname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]

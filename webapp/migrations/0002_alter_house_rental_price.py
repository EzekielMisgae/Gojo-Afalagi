# Generated by Django 4.1.5 on 2023-01-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='rental_price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]

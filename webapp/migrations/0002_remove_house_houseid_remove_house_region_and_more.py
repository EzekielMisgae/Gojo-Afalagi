# Generated by Django 4.1.5 on 2023-01-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='houseID',
        ),
        migrations.RemoveField(
            model_name='house',
            name='region',
        ),
        migrations.AddField(
            model_name='house',
            name='kebele',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='numRoom',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(choices=[('AddisAbaba', 'AddisAbaba'), ('Bahirdar', 'Bahirdar'), ('DireDawa', 'DireDawa'), ('Harar', 'Harar'), ('Mekele', 'Mekele'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_house_houseid_remove_house_region_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='region',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='job',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.FileField(default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('AddisAbaba', 'AddisAbaba'), ('Bahirdar', 'Bahirdar'), ('DireDawa', 'DireDawa'), ('Harar', 'Harar'), ('Mekele', 'Mekele'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]
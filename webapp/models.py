from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    REGION = (
        ('AddisAbaba', 'AddisAbaba'),
        ('Afar', 'Afar'),
        ('Amhara', 'Amhara'),
        ('Benishangul', 'Benishangul'),
        ('DireDawa', 'DireDawa'),
        ('Gambella', 'Gambella'),
        ('Harari', 'Harari'),
        ('Oromia', 'Oromia'),
        ('Somali', 'Somali'),
        ('SWEPR', 'SWEPR'),
        ('SNNPR', 'SNNPR'),
        ('Tigray', 'Tigray'),
    )
    username = models.CharField(max_length=255,null=False)
    email = models.CharField(max_length=255,null=False)
    phone = models.CharField(max_length=11,null=True)
    password = models.CharField(max_length=255,null=False)
    kebele = models.IntegerField
    kebeleID = models.CharField(max_length=10, null=True, default=0) 
    region = models.CharField(max_length=100, choices=REGION)
    city = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)

class House(models.Model):
    REGION = (
        ('Afar', 'Afar'),
        ('Amhara', 'Amhara'),
        ('Benishangul', 'Benishangul'),
        ('Gambella', 'Gambella'),
        ('Harari', 'Harari'),
        ('Oromia', 'Oromia'),
        ('Somali', 'Somali'),
        ('SWEPR', 'SWEPR'),
        ('SNNPR', 'SNNPR'),
        ('Tigray', 'Tigray'),
    )
    HOUSESTATUS = (
        ('Available', 'Available'),
        ('Rented', 'Rented')
    )
    HOUSETYPE = (
        ('Apartment', 'Apartment'),
        ('Compound', 'Compound'),
        ('Room', 'Room'),
        ('Condominium', 'Condominium'),
        ('Luxury', 'Luxury')
    )
    houseID = models.IntegerField(null=False)
    housetype = models.CharField(max_length=255, choices=HOUSETYPE, null=True)
    numRoom = models.IntegerField
    kebele = models.IntegerField
    region = models.CharField(max_length=100, choices=REGION)
    city = models.CharField(max_length=255,null=True)
    area = models.FloatField(null=True)
    price = models.IntegerField(null=True)
    floor = models.IntegerField(null=True, default=0)
    landlordName = models.CharField(max_length=255,null=True)
    landlordPhone = models.CharField(max_length=255, null=True)
    houseStatus = models.CharField(max_length=200, default='Available' ,choices=HOUSESTATUS)

class Book(models.Model):
    PAYOPTION = (
        ('Cash', 'Cash'),
        ('Telebirr', 'Telebirr'),
        ('CBE birr', 'CBE birr'),
        ('Bank', 'Bank'),
        ('Other', 'Other'),
    )
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=False)
    paymentOption = models.BooleanField(null=False, choices=PAYOPTION)
    kebeleID = models.IntegerField(null=False)

class Picture(models.Model):
    pic = models.FileField(upload_to='',null=True,default='')
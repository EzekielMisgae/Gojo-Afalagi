from django.db import models

# Create your models here.

class User(models.Model):
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
    UserID = models.AutoField(primary_key=True,null=False)
    Username = models.CharField(max_length=255,null=False)
    Email = models.CharField(max_length=255,null=False)
    Phone = models.CharField(max_length=11,null=True)
    Password = models.CharField(max_length=255,null=False)
    Kebele = models.IntegerField
    KebeleID = models.CharField(max_length=10, null=True, default=0) 
    Region = models.CharField(max_length=100, choices=REGION)
    City = models.CharField(max_length=255,null=True)
    Address = models.CharField(max_length=255,null=True)
    Profile = models.FileField(upload_to='',null=True,default='') 
    Login = models.BooleanField(null=False,default=False)
    Job = models.CharField(max_length=255,null=True)
    Introduction = models.TextField(null=True)

class Info(models.Model):
    InfoID = models.AutoField(primary_key=True,null=False)
    Datetime = models.DateTimeField(null=False)
    UserID = models.IntegerField(null=False) 
    KebeleID = models.IntegerField(null=True)

class House(models.Model):
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

    HouseID = models.AutoField(primary_key=True,null=False)
    Housetype = models.CharField(max_length=255, choices=HOUSETYPE, null=True)
    NumRoom = models.IntegerField
    Kebele = models.IntegerField
    Region = models.CharField(max_length=100, choices=REGION)
    City = models.CharField(max_length=255,null=True)
    Address = models.CharField(max_length=255,null=True)
    Area = models.FloatField(null=True)
    Price = models.IntegerField(null=True)
    Floor = models.IntegerField(null=True)
    LandlordName = models.CharField(max_length=255,null=True)
    LandlordPhone = models.CharField(max_length=255, null=True)
    Introduction = models.TextField(null=True, default="")
    HouseStatus = models.CharField(max_length=200, choices=HOUSESTATUS)

class Order(models.Model):
    PAYOPTION = (
        ('Cash', 'Cash'),
        ('Telebirr', 'Telebirr'),
        ('CBE birr', 'CBE birr'),
        ('Bank', 'Bank'),
        ('Other', 'Other'),
    )

    OrderID = models.AutoField(primary_key=True,null=False)
    OrderDate = models.DateTimeField(null=False)
    DueDate = models.DateTimeField(null=False)
    Price = models.IntegerField(null=False)
    PaymentOption = models.BooleanField(null=False, choices=PAYOPTION)
    UserID = models.IntegerField(null=False)
    HouseID = models.IntegerField(null=False)
    KebeleID = models.IntegerField(null=False)

class Message(models.Model):
    MessageID = models.AutoField(primary_key=True,null=False)
    WorkID = models.IntegerField(null=True) 
    Errornumber = models.IntegerField(null=True)
    UserID = models.IntegerField(null=False)
    Text = models.TextField(null=True)
    Username = models.CharField(max_length=255,null=False)

class Picture(models.Model):
    PicID = models.AutoField(primary_key=True,null=False)
    Pic = models.FileField(upload_to='',null=True,default='')
    UserID = models.IntegerField(null=True)
    HouseID = models.IntegerField(null=True)
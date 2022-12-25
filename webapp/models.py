from django.db import models

# Create your models here.

class Customer(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    CUSTOMERTYPE = (
        ('Owner', 'Owner'),
        ('Renter', 'Renter')
    )

    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=6, null=True, choices=SEX)
    phoneNum = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    customer_type = models.CharField(max_length=100, null=True, choices=CUSTOMERTYPE)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.firstName


class houseTag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class House(models.Model):

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

    numRoom = models.IntegerField(null=True)
    kebele = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True, choices=REGION)
    price = models.IntegerField(null=True)
    houseType = models.CharField(max_length=100, null=True, choices=HOUSETYPE)
    house_status = models.CharField(max_length=200, null=True, choices=HOUSESTATUS)
    description = models.CharField(max_length=100, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.houseType


class Status(models.Model):
    status = models.CharField(max_length=100, null=True)
    customer = models.CharField(max_length=100, null=True)
    House = models.CharField(max_length=100, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.status


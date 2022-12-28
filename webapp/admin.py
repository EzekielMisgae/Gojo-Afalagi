from django.contrib import admin
from .models import House,Info,Picture,Message
from .models import Order,User

admin.site.register(Order)
admin.site.register(User)
admin.site.register(House)
admin.site.register(Info)
admin.site.register(Picture)
admin.site.register(Message)

# from django.contrib import admin
# from .import models


# # Register your models here.
# @admin.register(models.POST)
# class Customer(models.Model):
#     SEX = (
#         ('Male', 'Male'),
#         ('Female', 'Female')
#     )
#     CUSTOMERTYPE = (
#         ('Owner', 'Owner'),
#         ('Renter', 'Renter')
#     )

#     firstName = models.CharField(max_length=100, null=True)
#     lastName = models.CharField(max_length=100, null=True)
#     sex = models.CharField(max_length=6, null=True, choices=SEX)
#     phoneNum = models.CharField(max_length=100, null=True)
#     email = models.CharField(max_length=100, null=True)
#     customer_type = models.CharField(max_length=100, null=True, choices=CUSTOMERTYPE)
#     dateCreated = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#        return self.firstName

# class houseTag(models.Model):
#     name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.name

# @admin.register(models.POST)
# class House(models.Model):

#     HOUSESTATUS = (
#         ('Available', 'Available'),
#         ('Rented', 'Rented')
#     )
#     HOUSETYPE = (
#         ('Apartment', 'Apartment'),
#         ('Compound', 'Compound'),
#         ('Room', 'Room'),
#         ('Condominium', 'Condominium'),
#         ('Luxury', 'Luxury')
#     )

#     REGION = (
#         ('AddisAbaba', 'AddisAbaba'),
#         ('Afar', 'Afar'),
#         ('Amhara', 'Amhara'),
#         ('Benishangul', 'Benishangul'),
#         ('DireDawa', 'DireDawa'),
#         ('Gambella', 'Gambella'),
#         ('Harari', 'Harari'),
#         ('Oromia', 'Oromia'),
#         ('Somali', 'Somali'),
#         ('SWEPR', 'SWEPR'),
#         ('SNNPR', 'SNNPR'),
#         ('Tigray', 'Tigray'),
#     )

#     numRoom = models.IntegerField
#     kebele = models.IntegerField
#     city = models.CharField(max_length=100)
#     region = models.CharField(max_length=100, choices=REGION)
#     price = models.IntegerField(null=True)
#     houseType = models.CharField(max_length=100, choices=HOUSETYPE)
#     house_status = models.CharField(max_length=200, choices=HOUSESTATUS)
#     description = models.CharField(max_length=100, blank=True)
#     dateCreated = models.DateTimeField(auto_now_add=True)
#     photo = models.ImageField(default='default.png', blank=True)

#     def __str__(self):
#         return self.houseType

# @admin.register(models.POST)
# class Status(models.Model):
#     status = models.CharField(max_length=100, null=True)
#     customer = models.CharField(max_length=100, null=True)
#     House = models.CharField(max_length=100, null=True)
#     dateCreated = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.status

# admin.site.register(Customer),
# admin.site.register(House),
# admin.site.register(Status),
# admin.site.register(houseTag),
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

	CITY = (
		('AddisAbaba', 'AddisAbaba'),
		('Bahirdar', 'Bahirdar'),
		('DireDawa', 'DireDawa'),
		('Harar', 'Harar'),
		('Mekele', 'Mekele'),
		('Other', 'Other'),
	)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	email = models.CharField(max_length=255, null=False)
	phone = models.CharField(max_length=11, null=True)
	kebeleID = models.CharField(max_length=10, null=True, default=0)
	city = models.CharField(max_length=100, choices=CITY,
							default='Other', null=False)
	job = models.CharField(max_length=255, null=True)
	fullName = models.CharField(max_length=100, null=True)

    
	def __str__(self):
		return self.fullName


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class House(models.Model):
    CITY = (
        ('AddisAbaba', 'AddisAbaba'),
        ('Bahirdar', 'Bahirdar'),
        ('DireDawa', 'DireDawa'),
        ('Harar', 'Harar'),
        ('Mekele', 'Mekele'),
        ('Other', 'Other'),
        )
    HOUSETYPE = (
        ('Apartment', 'Apartment'),
        ('Compound', 'Compound'),
        ('Room', 'Room'),
        ('Condominium', 'Condominium'),
        ('Luxury', 'Luxury')
    )
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=False)
    house_type = models.CharField(max_length=255, default='Room', choices=HOUSETYPE, null=True)
    city = models.CharField(max_length=100, choices=CITY, default='Other', null=False)
    bedrooms = models.IntegerField(blank=True, null=False)
    rental_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    image = models.ImageField(upload_to='houses/')
    tags = models.ManyToManyField(Tag)
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

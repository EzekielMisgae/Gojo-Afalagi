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
		return self.user


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
    housetype = models.CharField(
        max_length=255, default='Room', choices=HOUSETYPE, null=True)
    numRoom = models.IntegerField(null=True)
    kebele = models.IntegerField(null=True)
    city = models.CharField(max_length=100, choices=CITY,
                            default='Other', null=False)
    area = models.FloatField(null=True)
    price = models.IntegerField(null=True)
    floor = models.IntegerField(null=True, default=0)
    landlordName = models.CharField(max_length=255, null=True)
    landlordPhone = models.CharField(max_length=20, null=True)
    houseStatus = models.CharField(
        max_length=100, default='Available', choices=HOUSESTATUS, null=False)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.housetype

    @property
    def imageURL(self):
        try:
            url = self.featured.url
        except:
            url = ''
        print('URL:', url)
        return url


class Book(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    house = models.ForeignKey(House, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=100, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.house.housetype


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

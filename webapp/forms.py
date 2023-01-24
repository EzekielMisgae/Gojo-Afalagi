from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class profileUpdate(ModelForm):
    class Meta:
        model = Customer
        fields = ['fullName', 'city', 'phone', 'kebeleID', 'job']


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = House
        fields = ('title', 'image')

# class ImageSave(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = House
#         fields = ('title', 'image')
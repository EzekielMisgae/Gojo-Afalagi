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
    fullName = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'fullName', 'email', 'password1', 'password2']


class profileUpdate(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fullName', 'phone', 'kebeleID', 'job', 'city']


class HouseForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = House
        fields = ('__all__')

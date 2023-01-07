from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import House
from .models import *

class BookFilter(ModelForm):
    class Meta:
        model = House
        fields = ['houseID']
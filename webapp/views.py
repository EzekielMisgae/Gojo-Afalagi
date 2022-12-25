from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def signin(request):
    signin = House.objects.all()     
    return render(request, 'accounts/first/signin.html', {'signin':signin})

def homepage(request):    
    return render(request, 'accounts/index.html', {})

def home(request):
    message = "Example Django project on vercel"
    return HttpResponse(message)


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        sex = request.POST['sex']
        phoneNum = request.POST['phoneNum']
        email = request.POST['email']
        customer_type = request.POST['customer_type']
        password = request.POST['password']

        if len(password) >= 8:
            messages.success('Successfully registered, please login to continue.')
            return redirect('accounts/first/signin.html')
        else:

            newMember = Customer(firstName=firstName, lastName=lastName, sex=sex, phoneNum=phoneNum, 
            email=email, customer_type=customer_type, password=password)
            newMember.save()

    return render(request, 'accounts/first/register.html', {})

def rentals(request):
    rentals = House.objects.all()
    return render(request, 'accounts/rentals.html', {'rentals':rentals})
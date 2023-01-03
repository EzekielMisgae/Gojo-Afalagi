from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .models import *
from .forms import BookForm, CreateUserForm
from .filters import BookFilter
from .decorators import unauthenticated_user, allowed_users, landlord_only

#create your views here
@unauthenticated_user
def landingPage(request):
    context = {}
    return render(request, 'accounts/first/landingPage.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('webapp:login')

    context = {'form':form}
    return render(request, 'accounts/first/register.html', context)

@unauthenticated_user #if users logged in already & try to access it will redirect them
def loginPage(request):
    if request.method == 'POST': #authenticate the username and password are existed
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('webapp:home')
        else:
            messages.info(request, 'Username OR password is incorrect!')
            return redirect('webapp:login')

    context = {}
    return render(request, 'accounts/first/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('webapp:login')

@login_required(login_url='webapp:login')#can't access without logging in
def homePage(request):
    context = {}
    return render(request, 'accounts/index.html', context)

@login_required(login_url='webapp:login')
def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='webapp:login')
@landlord_only
def rentals(request):
    rentals = House.objects.all()
    return render(request, 'accounts/allHouse.html', {'rentals':rentals})

@login_required(login_url='webapp:login')
def contact(request):
    context = {}
    return render(request, 'accounts/contact.html', context)

@login_required(login_url='webapp:login')
def about(request):
    context = {}
    return render(request, 'accounts/about.html', context)
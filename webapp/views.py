from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import *
from .forms import CreateUserForm, profileUpdate
from .forms import HouseForm
from .decorators import unauthenticated_user, staff_only


### =======> Related Login and Registration Pages<======== ###

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            fullName = form.cleaned_data.get('fullName')
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            #Added fullName 
            Customer.objects.create(
                user=user,
                fullName=fullName,
                )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/first/register.html', context)

@unauthenticated_user  # if users logged in already & try to access it will redirect them
def loginPage(request):
    if request.method == 'POST':  # authenticate the username and password are existed
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect!')
            return redirect('login')
    context = {}
    return render(request, 'accounts/first/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('landingPage')

### =======> ///Related Login and Registration Pages///<======== ###



### =======> Related to Home and landing Pages<======== ###

@unauthenticated_user   # if users logged in already & try to access it will redirect them
def landingPage(request):
    context = {}
    return render(request, 'accounts/first/landingPage.html', context)

@login_required(login_url='login')  # can't access without logging in
def homePage(request):
    houses = House.objects.all()
    return render(request, 'accounts/index.html', {'houses': houses})

### =======> ///Related to Home and landing Pages///<======== ###



### =======> Related to Customer Profile and About <======== ###
@login_required(login_url='login')
def profile(request):
    user = request.user
    if user.is_authenticated:
        customer = get_object_or_404(Customer, user=user)
        form = profileUpdate(instance=customer)
        if request.method == 'POST':
            form = profileUpdate(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('profile')
        context = {'form':form, 'customer':customer}
        return render(request, 'accounts/profile.html', context)
    else:
        messages.warning(request, 'You need to login first')
        return redirect('login')

def about(request):
    context = {}
    return render(request, 'accounts/about.html', context)

def aboutme(request):
    context = {}
    return render(request, 'accounts/aboutme.html', context)

### =======> ///Related to Customer and About/// <======== ###



### =======> Related to type of house <======= ###

@login_required(login_url='login')
def compound(request):
    houses = House.objects.filter(house_type='Compound')
    context = {'houses': houses}
    return render(request, 'accounts/rental/compound.html', context)

@login_required(login_url='login')
def apartment(request):
    houses = House.objects.filter(house_type='Apartment')
    context = {'houses': houses}
    return render(request,'accounts/rental/apartment.html', context)

@login_required(login_url='login')
def room(request):
    houses = House.objects.filter(house_type='Room')
    context = {'houses': houses}
    return render(request,'accounts/rental/room.html', context)

@login_required(login_url='login')
def condominium(request):
    houses = House.objects.filter(house_type='Condominium')
    context = {'houses': houses}
    return render(request,'accounts/rental/condominium.html', context)

@login_required(login_url='login')
def luxurious(request):
    houses = House.objects.filter(house_type='Luxury')
    context = {'houses': houses}
    return render(request,'accounts/rental/luxurious.html', context)

### =======> ///Related to type of house/// <======= ###



### =======> Related to House upload/// <======= ###
@login_required(login_url='login')
def house_list(request):
    houses = House.objects.all()
    return render(request, 'accounts/list.html', {'houses': houses})

@login_required(login_url='login')
def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'accounts/detail.html', {'house': house})

@login_required(login_url='login')
@staff_only
def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('house_list')
    else:
        form = HouseForm()
        context = {'form': form}
    return render(request, 'accounts/form.html', context)

### =======> ///Related to House upload/// <======= ###
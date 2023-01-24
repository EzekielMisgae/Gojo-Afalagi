from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm, profileUpdate
from .forms import ImageForm
from .decorators import unauthenticated_user, allowed_users, landlord_only


### =======> Related Login and Registration Pages<======== ###

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			# group = Group.objects.get(name='customer')
			# user.groups.add(group)
			#Added username because of error returning customer name if not added
			Customer.objects.create(
				user=user,
				fullName=user.username,
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
    compound = House.objects.filter(housetype="Compound")
    apartment = House.objects.filter(housetype="Apartment")
    condominium = House.objects.filter(housetype="Condominium")
    luxury = House.objects.filter(housetype="Luxury")
    rooms = House.objects.filter(housetype="Room")
    context = {'houses':houses, 'compound':compound, 'apartment':apartment, 'condominium':condominium, 'luxury':luxury, 'rooms':rooms}
    return render(request, 'accounts/index.html', context)

### =======> ///Related to Home and landing Pages///<======== ###



### =======> Related to Customer Profile and About <======== ###

@login_required(login_url='login')
def profile(request):
    # import pdb; pdb.set_trace()
    customerById = Customer.objects.get(user=request.user)
    
    form = profileUpdate(instance=customerById)
    
    if request.method == 'POST':
        form = profileUpdate(request.POST, instance=customerById)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            
            form.save()
            name = form.cleaned_data.get('fullName')

            messages.success(request, 'Account updated successfully for ' + name)

            return redirect('profile')
    context = {'form':form, 'customerById':customerById}
    return render(request, 'accounts/profile.html', context)


def about(request):
    context = {}
    return render(request, 'accounts/about.html', context)

def aboutme(request):
    context = {}
    return render(request, 'accounts/aboutme.html', context)

### =======> ///Related to Customer and About/// <======== ###




### =======> Related to type of house <======= ###

@login_required(login_url='login')
def rentals(request):
    list = House.objects.all()
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'accounts/rental/apartment.html', {'form': form, 'list':list, 'img_obj': img_obj})
    else:
        form = ImageForm()
        # form.save()
    return render(request, 'accounts/rentalSec.html', {'form': form})


@login_required(login_url='login')
def house(request):
    houses = House.objects.filter(housetype='Compound')
    context = {'houses':houses}
    return render(request, 'accounts/rental/house.html', context)


@login_required(login_url='login')
def apartment(request):
    houses = House.objects.filter(housetype="Apartment")
    context = {'houses':houses}
    return render(request,'accounts/rental/apartment.html', context)


@login_required(login_url='login')
def room(request):
    list = House.objects.filter(housetype="Room")

    return render(request,'accounts/rental/room.html',{'list':list})


@login_required(login_url='login')
def condominium(request):
    list = House.objects.filter(housetype="Condominium")

    return render(request,'accounts/rental/condominium.html',{'list':list})


@login_required(login_url='login')
def luxurious(request):
    list = House.objects.filter(housetype="Luxury")

    return render(request,'accounts/rental/luxurious.html',{'list':list})

### =======> ///Related to type of house/// <======= ###



#### =======> Related to customers <======== ####


def ImageSave(request):
    HouseId = House.objects.get(image=request.image)
    form = ImageForm(instance=HouseId)
    if request.method == 'POST':
        form = ImageSave(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            return render(request, 'accounts/rental/apartment.html', {'form': form, 'img_obj': img_obj})

            # return redirect('rentals')
    context = {'form':form}
    return render(request, 'accounts/rentals.html', context)



# @login_required(login_url='login')
# def search(city, numRoom, area, houseType):
#     houses = House.objects.all()

#     if city:
#         houses = houses.filter(city=city)
#     if numRoom:
#         houses = houses.filter(numRoom=numRoom)
#     if area:
#         houses = houses.filter(area=area)
#     if houseType:
#         houses = houses.filter(houseType=houseType)

#     return houses

#### =======> ///Related to customers/// <======== ####
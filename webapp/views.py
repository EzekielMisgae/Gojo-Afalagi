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
from .forms import BookForm, CreateUserForm, CustomerForm, ImageForm, profileUpdate
from .filters import BookFilter
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


# @unauthenticated_user
# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')

#             messages.success(request, 'Account was created for ' + username)

#             return redirect('login')
#     context = {'form': form}
#     return render(request, 'accounts/first/register.html', context)


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
    context = {}
    return render(request, 'accounts/index.html', context)

### =======> ///Related to Home and landing Pages///<======== ###



### =======> Related to Customer Profile and About <======== ###

@login_required(login_url='login')
def profile(request):
    form = profileUpdate()
    if request.method == 'POST':
        form = profileUpdate(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account updated successfully for ' + username)

            return redirect('profile')
    context = {}
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
    rentals = House.objects.all()
    return render(request, 'accounts/rentals.html', {'rentals': rentals})


@login_required(login_url='login')
def house(request):
    houses = House.objects.filter(housetype="house")
    return render(request, 'accounts/rental/house.html', {'houses':houses})


@login_required(login_url='login')
def apartment(request):
	apartments = House.objects.filter(housetype="apartment")
	return render(request, 'accounts/rental/apartment.html', {'apartments':apartments})


@login_required(login_url='login')
def room(request):
	rooms = House.objects.filter(housetype="room")
	return render(request, 'accounts/rental/room.html', {'rooms':rooms})


@login_required(login_url='login')
def condominium(request):
    condos = House.objects.filter(housetype="condominium")
    totalCondo = condos.count()
    rented = condos.filter(houseStatus='Rented')
    available = condos.filter(houseStatus='Available')
    context = {'rented': rented, 'available': available, 'totalCondo': totalCondo}
    return render(request, 'accounts/rental/condominium.html', context)


@login_required(login_url='login')
def luxurious(request):
    luxury = House.objects.filter(housetype="luxury")
    totalLux = luxury.count()
    rented = luxury.filter(houseStatus='Rented')
    available = luxury.filter(houseStatus='Available')
    context = {'rented': rented, 'available': available, 'totalLux': totalLux,}
    return render(request, 'accounts/rental/luxurious.html', context)


### =======> ///Related to type of house/// <======= ###



#### =======> Related to customers <======== ####


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            messages.success(request, 'Image uploaded succefully!')

            return render(request, 'accounts/rentals.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'accounts/rentals.html', {'form': form})


@login_required(login_url='login')
def search(city, numRoom, area, houseType):
    houses = House.objects.all()

    if city:
        houses = houses.filter(city=city)
    if numRoom:
        houses = houses.filter(numRoom=numRoom)
    if area:
        houses = houses.filter(area=area)
    if houseType:
        houses = houses.filter(houseType=houseType)

    return houses

#### =======> ///Related to customers/// <======== ####



#### =======> Related to Book <======== ####

@login_required(login_url='login')
@allowed_users
def createBook(request, id):
    # extra = 5
    BookFormSet = inlineformset_factory(
        Customer, Book, fields=('House', 'status',), extra=5)
    customers = Customer.objects.get(id=id)

    # queryset=Book.objects.none()
    formset = BookFormSet(queryset=Book.objects.none(), instance=customers)

    # form = BookForm(initial={'customer': customers})
    if request.method == 'POST':
        # form = BookForm(request.POST)
        formset = BookFormSet(request.POST, instance=customers)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/create_book.html', context)


@login_required(login_url='login')
@allowed_users
def updateBook(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'book': book, 'form': form}
    return render(request, 'accounts/update_book.html', context)

@login_required(login_url='login')
@allowed_users
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('/')

    context = {'book': book}
    return render(request, 'accounts/delete_book.html', context)

### =======> ///Related to Book/// <======== ####
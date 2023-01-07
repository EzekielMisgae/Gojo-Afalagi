from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .models import *
from .forms import BookForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, landlord_only

# create your views here


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
            messages.success(request, 'Account was created for ' + user)
            return redirect('webapp:login')

    context = {'form': form}
    return render(request, 'accounts/first/register.html', context)

@unauthenticated_user  # if users logged in already & try to access it will redirect them
def loginPage(request):
    if request.method == 'POST':  # authenticate the username and password are existed
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
    return redirect('webapp:landingPage')


@login_required(login_url='webapp:login')  # can't access without logging in
def homePage(request):
    context = {}
    return render(request, 'accounts/index.html', context)


@login_required(login_url='webapp:login')
def profile(request):
    books = request.user.customer.book_set.all()
    print('BOOKS:', books)
    context = {'books':books}
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='webapp:login')
def rentals(request):
    rentals = House.objects.all()
    return render(request, 'accounts/rentals.html', {'rentals': rentals})


@login_required(login_url='webapp:login')
def contact(request):
    context = {}
    return render(request, 'accounts/contact.html', context)


def about(request):
    context = {}
    return render(request, 'accounts/about.html', context)


def aboutme(request):
    context = {}
    return render(request, 'accounts/aboutme.html', context)


@login_required(login_url='webapp:login')
def updateBook(request, pk):
    books = Book.objects.get(id=pk)
    form = Book.form(instance=books)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/book_form.html', context)


@login_required(login_url='webapp:login')
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    context = {'house': book}
    return render(request, 'accounts/delete_book.html', context)


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

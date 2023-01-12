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
    context = {}
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
    # customerById = House.objects.get(user=request.title)
    
    # form = profileUpdate(instance=customerById)
    
    # if request.method == 'POST':
    #     form = profileUpdate(request.POST, instance=customerById)
    #     # import pdb; pdb.set_trace()
    #     if form.is_valid():
            
    #         form.save()
    #         title = form.cleaned_data.get('title')

    #         messages.success(request, 'Account updated successfully for ' + title)

    #         return redirect('rentals')
    # context = {'form':form, 'customerById':customerById}
    # return render(request, 'accounts/rentals.html', context)


    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'accounts/rental/apartment.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
        # form.save()
    return render(request, 'accounts/rentalSec.html', {'form': form})


# @login_required(login_url='login')
# def rentals(request):
#     rentals = House.objects.all()
#     return render(request, 'accounts/rentals.html', {'rentals': rentals})


@login_required(login_url='login')
def house(request):
    i = House.objects.all(image)
    
    houses = House.objects.filter(housetype="Compound")
    image = House.objects.filter(image)
    return render(request, 'accounts/rental/house.html', {'houses':houses, 'image':image})


@login_required(login_url='login')
def apartment(request):
    list = House.objects.filter(housetype="Apartment")

    return render(request,'accounts/rental/apartment.html',{'list':list})


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

# @login_required(login_url='login')
# @allowed_users
# def createBook(request, id):
#     # extra = 5
#     BookFormSet = inlineformset_factory(
#         Customer, Book, fields=('House', 'status',), extra=5)
#     customers = Customer.objects.get(id=id)

#     # queryset=Book.objects.none()
#     formset = BookFormSet(queryset=Book.objects.none(), instance=customers)

#     # form = BookForm(initial={'customer': customers})
#     if request.method == 'POST':
#         # form = BookForm(request.POST)
#         formset = BookFormSet(request.POST, instance=customers)
#         if formset.is_valid():
#             formset.save()
#             return redirect('/')

#     context = {'formset': formset}
#     return render(request, 'accounts/create_book.html', context)


# @login_required(login_url='login')
# @allowed_users
# def updateBook(request, id):
#     book = Book.objects.get(id=id)
#     form = BookForm(instance=book)

#     if request.method == "POST":
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'book': book, 'form': form}
#     return render(request, 'accounts/update_book.html', context)

# @login_required(login_url='login')
# @allowed_users
# def deleteBook(request, pk):
#     book = Book.objects.get(id=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect('/')

#     context = {'book': book}
#     return render(request, 'accounts/delete_book.html', context)

### =======> ///Related to Book/// <======== ####


# def search(request):
#     template = loader.get_template('home.html')
#     context = {}
#     if request.method == 'GET':
#         typ = request.GET['type']
#         q = request.GET['q']
#         context.update({'type': typ})
#         context.update({'q':q})
#         results={}
#         if typ == 'House' and (bool(House.objects.filter(location=q)) or bool(House.objects.filter(city=q))):
#             results = House.objects.filter(location=q)
#             results = results | House.objects.filter(city=q)
#         elif typ == 'Apartment'  and (bool(Room.objects.filter(location=q)) or bool(House.objects.filter(city=q))):
#             results = Room.objects.filter(location=q)
#             results = results | Room.objects.filter(city=q)

        
#         if bool(results)== False:
#             print("messages")
#             messages.success(request, "No matching results for your query..")

#         result = [results, len(results)]
#         context.update({'result': result})

#     return HttpResponse(template.render(context, request))
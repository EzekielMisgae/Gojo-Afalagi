# encoding:utf-8
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.conf.global_settings import MEDIA_ROOT
import re
import json
from .models import *
import datetime
from django.core import serializers
import shutil
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def FirstPage(request): #Main interface
    if request.method == 'POST':  # Determine whether the request method is POST (POST mode required)
        querylist = request.POST
        function_id = querylist.get('function_id')
        user_id = querylist.get('user_id')
        user = User.objects.get(UserID=user_id)
        if function_id == '0':  # My Orders
            orderlist = []
            order = Order.objects.filter(UserID=user_id,Pay=False)
            #If the user doesn't have an order?
            for x in order:
                y = House.objects.get(HouseID=x.HouseID)
                orderlist.append({
                    'OrderDate':x.OrderDate.date(),
                    'OrderID': x.OrderID,
                    'HouseID': x.HouseID,
                    'LandlordName': y.LandlordName,
                    'LandlordPhone': y.LandlordPhone,
                    'Address': y.Address
                })
            return JsonResponse({'orderlist': orderlist})
        elif function_id == '3':  # Personal Data
            return JsonResponse({'introduction': user.Introduction})
        elif function_id == '4': # Home page
            houselist = []
            allhouse = House.objects.filter()
            for x in allhouse:
                pics = Picture.objects.filter(HouseID=x.HouseID).values('PicPath')
                house = House.objects.get(HouseID=x.HouseID)
                houselist.append({
                    'HouseID': x.HouseID,
                    'Housename': house.Housename,
                    'Floor':house.Floor,
                    'PicPathList': list(pics),
                    'Address': house.Address,
                    'Area': house.Area,
                    'Housetype': house.Housetype,
                    'Rent': house.Rent,
                })
            return JsonResponse({'houselist':houselist})
        elif function_id == '5': #View
            house_id = querylist.get('house_id')
            house = House.objects.get(HouseID=house_id)
            picturelist = []
            for x in Picture.objects.filter(HouseID=house_id):
                picturelist.append({
                    'PicPathList': x.PicPath
                })
            return JsonResponse({'Mark':house.Mark,
                                 'HouseID':house.HouseID,
                                 'Housename':house.Housename,
                                 'Rent':house.Rent,
                                 'Housetype': house.Housetype,
                                 'Area': house.Area,
                                 'Floor': house.Floor,
                                 'Type': house.Type,
                                 'LandlordPhone': house.LandlordPhone,
                                 'Introduction': house.Introduction,
                                 'Picturelist': picturelist
                                 })

@csrf_exempt
def Register(request):
    if request.method == 'POST': #Determine whether the request mode is POST (POST mode required)
        querylist = request.POST
        function_id = querylist.get('function_id')
        if function_id == '1':
            email = querylist.get('email')
            username = querylist.get('username')
            password_1 = querylist.get('password_1')
            password_2 = querylist.get('password_2')
            email = querylist.get('email')
            if(User.objects.filter(Username=username).exists() or User.objects.filter(Email=email).exists()):
                return JsonResponse({'errornumber': 3, 'message': "The username or email address already exists"})
            elif(re.match("^[A-Za-z0-9]+$",password_1)==None): 
                return JsonResponse({'errornumber': 4, 'message': "Only letters and numbers"})
            elif(password_1 != password_2):
                return JsonResponse({'errornumber': 5, 'message': "Password don't match"})
            elif(re.match("^([a-zA-Z\d][\w-]{2,})@(\w{2,})\.([a-z]{2,})(\.[a-z]{2,})?$",email)==None):
                return JsonResponse({'errornumber': 7, 'message': "Wrong Email format"})
            else:
                new_user = User(Username=username,Password=password_1,Email=email,Status='Y')
                new_user.save()
                return JsonResponse({'errornumber': 0, 'message': "Registration successful",'user_id':new_user.UserID,'username':new_user.Username})
    else:
        return JsonResponse({'errornumber': 1, 'message': "Bad request"})

@csrf_exempt
def Login(request):
    if request.method == 'POST': 
        querylist = request.POST
        password = querylist.get('password')
        email = querylist.get('email')
        if User.objects.filter(Email=email).exists() == True:
            loginuser = User.objects.get(Email=email)
        else:
            return JsonResponse({'errornumber': 3, 'message': "The user does not exist, please register"})
            #Registration guarantees username and email only一
        if(loginuser.Password!=password):
            return JsonResponse({'errornumber': 4, 'message': "The password is wrong, please try again"})
        elif(loginuser.Password==password):
            if(loginuser.Status=='Y'):
                return JsonResponse({'errornumber': 0, 'message': "Welcome!",'User_id':loginuser.UserID,'Username':loginuser.Username,'avatar_url':loginuser.avatar_url})
    else:
        return JsonResponse({'error': 5, 'message': "Bad request"})

@csrf_exempt
def user(request):
    if request.method == 'POST':
        querylist = request.POST
        function_id = querylist.get('function_id')
        user_id = querylist.get('user_id')
        user = User.objects.get(UserID=user_id)
        if function_id == '0':  # My orders
            orderlist = []
            order = Order.objects.filter(UserID=user_id,Pay=False)
            for x in order:
                y = House.objects.get(HouseID=x.HouseID)
                orderlist.append({
                    'OrderDate': x.OrderDate.date(),
                    'OrderID': x.OrderID,
                    'HouseID': x.HouseID,
                    'LandlordName': y.LandlordName,
                    'LandlordPhone': y.LandlordPhone,
                    'Address': y.Address
                })
            return JsonResponse({'orderlist': orderlist})
        
        elif function_id == '3':  # # Profile
            return JsonResponse({'introduction': user.Introduction})
        elif function_id == '4':  # Home Page
            return JsonResponse()
        elif function_id == '5': #Details
            return JsonResponse({'avatar_url':user.avatar_url,'Username':user.Username,'Phone':user.Phone,'City':user.City,'Job':user.Job})
        elif function_id == '6': #Update profile
            user = User.objects.get(UserID=user_id)
            user.Introduction = querylist.get('introduction')
            user.save()
            return JsonResponse({'introduction': user.Introduction})
        elif function_id == '7': #Update your profile
            user.Username = querylist.get('Username')
            user.Phone = querylist.get('Phone')
            user.City = querylist.get('City')
            user.Job = querylist.get('Job')
            user.save()
            return JsonResponse({'Username': user.Username, 'Phone': user.Phone, 'City': user.City,'Job': user.Job,'avatar':user.avatar.name})
        elif function_id == '8': #Update profile
            avatar = request.FILES.get('avatar')
            suffix = '.' + avatar.name.split('.')[-1]
            avatar.name = str(user_id)+'avatar'+suffix
            user.avatar= avatar
            user.save()
            user.avatar_url = "http://127.0.0.1:8000/media/" + user.avatar.name
            user.save()
            return JsonResponse({'avatar_url': user.avatar_url})
    else:
        return JsonResponse({'errornumber': 2, 'message': "Bad request"})


@csrf_exempt
def FirstPage(request): #Main interface
    if request.method == 'POST': # Determine whether the request method is POST (POST mode required)
        querylist = request.POST
        function_id = querylist.get('function_id')
        user_id = querylist.get('user_id')
        user = User.objects.get(UserID=user_id)
        if function_id == '0': # My Orders
            orderlist = []
            order = Order.objects.filter(UserID=user_id, Pay=False)
            # If the user has no order?
            for x in order:
                y = House.objects.get(HouseID=x.HouseID)
                orderlist.append({
                    'OrderDate': x.OrderDate.date(),
                    'OrderID': x.OrderID,
                    'HouseID': x.HouseID,
                    'LandlordName': y.LandlordName,
                    'LandlordPhone': y.LandlordPhone,
                    'Address': y.Address
                })
            return JsonResponse({'orderlist': orderlist})

        elif function_id == '3': # Profile
            return JsonResponse({'introduction': user.Introduction})
        elif function_id == '4': # Home page
            houselist = []
            allhouse = House.objects.filter()
            for x in allhouse:
                pics = Picture.objects.filter(
                    HouseID=x.HouseID).values('PicPath')
                house = House.objects.get(HouseID=x.HouseID)
                houselist.append({
                    'HouseID': x.HouseID,
                    'Housename': house.Housename,
                    'Floor': house.Floor,
                    'PicPathList': list(pics),
                    'Address': house.Address,
                    'Area': house.Area,
                    'Housetype': house.Housetype,
                    'Rent': house.Rent,
                })
            return JsonResponse({'houselist': houselist})
        elif function_id == '5': # View
            house_id = querylist.get('house_id')
            house = House.objects.get(HouseID=house_id)
            picturelist = []
            for x in Picture.objects.filter(HouseID=house_id):
                picturelist.append({
                    'PicPathList': x.PicPath
                })
            return JsonResponse({'Mark': house.Mark,
                                 'HouseID': house.HouseID,
                                 'Housename': house.Housename,
                                 'Rent': house.Rent,
                                 'Housetype': house.Housetype,
                                 'Area': house.Area,
                                 'Floor': house.Floor,
                                 'Type': house.Type,
                                 'LandlordPhone': house.LandlordPhone,
                                 'Introduction': house.Introduction,
                                 'Picturelist': picturelist
                                 })

@csrf_exempt
def search(request): #If to rent
    if request.method == 'POST':  # Determine whether the request method is POST (POST mode required)
        querylist = request.POST
        function_id = querylist.get('function_id')
        user_id = querylist.get('user_id')
        user = User.objects.get(UserID=user_id)
        if function_id == '0':  # My Orders
            orderlist = []
            order = Order.objects.filter(UserID=user_id,Pay=False)
            #If the user doesn't have an order?
            for x in order:
                y = House.objects.get(HouseID=x.HouseID)
                orderlist.append({
                    'OrderDate':x.OrderDate.date(),
                    'OrderID': x.OrderID,
                    'HouseID': x.HouseID,
                    'LandlordName': y.LandlordName,
                    'LandlordPhone': y.LandlordPhone,
                    'Address': y.Address
                })
            return JsonResponse({'orderlist': orderlist})
        elif function_id == '3':  # Personal Data
            return JsonResponse({'introduction': user.Introduction})
        elif function_id == '4': # Home page
            houselist = []
            allhouse = House.objects.filter()
            for x in allhouse:
                pics = Picture.objects.filter(HouseID=x.HouseID).values('PicPath')
                house = House.objects.get(HouseID=x.HouseID)
                houselist.append({
                    'HouseID': x.HouseID,
                    'Housename': house.Housename,
                    'Floor':house.Floor,
                    'PicPathList': list(pics),
                    'Address': house.Address,
                    'Area': house.Area,
                    'Housetype': house.Housetype,
                    'Rent': house.Rent,
                })
            return JsonResponse({'houselist':houselist})
        elif function_id == '5': #View
            house_id = querylist.get('house_id')
            house = House.objects.get(HouseID=house_id)
            return JsonResponse({'Mark':house.Mark,
                                 'HouseID':house.HouseID,
                                 'Housename':house.Housename,
                                 'Rent':house.Rent,
                                 'Housetype': house.Housetype,
                                 'Area': house.Area,
                                 'Floor': house.Floor,
                                 'Type': house.Type,
                                 'LandlordPhone': house.LandlordPhone,
                                 'Introduction': house.Introduction})
        elif function_id == '6': # collection
            house_id = querylist.get('house_id')
            house = House.objects.get(HouseID=house_id)
            if UserHouse.objects.filter(UserID=user_id,HouseID=house_id).exists() == True:
                return JsonResponse({'errornumber': 3, 'message': "Favorites"})
            else:
                new_collection = UserHouse(UserID=user_id,HouseID=house_id,Mark=house.Mark)
                new_collection.save()
                return JsonResponse({'errornumber': 1, 'message': "Log in successfully and bookmark!"})# Unsuccessful login is temporarily handled by the frontend
        elif function_id == '7': #Listing search
            house_name = querylist.get('house_name')
            houses = House.objects.filter(Housename__contains=house_name)
            # return JsonResponse(list(response), safe=False, json_dumps_params={'ensure_ascii': False})
            houselist = []
            for house in houses:
                pics = Picture.objects.filter(HouseID=house.HouseID).values('PicPath')
                houselist.append({
                    'HouseID': house.HouseID,
                    'PicPathList': list(pics),
                    'Address': house.Address,
                    'Area': house.Area,
                    'Housetype': house.Housetype,
                    'Rent': house.Rent,
                    'Floor': house.Floor,
                    'Housename': house.Housename
                })
            return JsonResponse({'houselist': houselist})
        elif function_id == '8': #Listing screening
            city = querylist.get('city')
            type = querylist.get('type')
            rent = querylist.get('rent')
            houses = House.objects.filter()
            if (city != 'undefined/undefined/undefined')and(city!='not/undefined/undefined'):
                lay = city.split('/')
                if lay[1] == '市辖区':
                    city = lay[0][:-1] + lay[2][:-1]
                else:
                    city = lay[1][:-1] + lay[2][:-1]
                houses = houses.filter(Address=city)
            if (type != '')and(type !='无'):
                houses = houses.filter(Housetype=type)

            if rent == '1':
                houses = houses.filter(Rent__lte=1000)
            if rent == '2':
                houses = houses.filter(Rent__gte=1000).filter(Rent__lte=3000)
            if rent == '3':
                houses = houses.filter(Rent__gte=3000).filter(Rent__lte=5000)
            if rent == '4':
                houses = houses.filter(Rent__gte=5000).filter(Rent__lte=10000)
            if rent == '5':
                houses = houses.filter(Rent__gte=10000)

            houselist = []
            for house in houses:
                pics = Picture.objects.filter(HouseID=house.HouseID).values('PicPath')
                houselist.append({
                    'HouseID': house.HouseID,
                    'PicPathList': list(pics),
                    'Address': house.Address,
                    'Area': house.Area,
                    'Housetype': house.Housetype,
                    'Rent': house.Rent,
                    'Floor': house.Floor,
                    'Housename': house.Housename
                })
            return JsonResponse({'houselist': houselist})
        elif function_id == '9': #Submit an application
            house_id = querylist.get('house_id')
            house = House.objects.get(HouseID=house_id,Status=False)
            start_day = datetime.datetime.strptime(querylist.get('start_day'), '%Y-%m-%d').date()
            finish_day = datetime.datetime.strptime(querylist.get('finish_day'), '%Y-%m-%d').date()
            day = (finish_day-start_day).days
            type = querylist.get('type')
            price = house.Rent*day
            if type == '1': #Short-term rentals
                return JsonResponse({'DayRent':house.Rent,'day':day,'Price':price})
            elif type == '2':
                return JsonResponse({'LandlordName':house.LandlordName,'Username':user.Username,'Address':house.Address,'Area':house.Area,'day':day,'starttime':str(start_day)})
    else:
        return JsonResponse({'errornumber': 2, 'message': "Bad reqest"})


@csrf_exempt
def order(request):
    if request.method == 'POST':  # Determine whether the request method is POST (POST mode required)
        querylist = request.POST
        function_id = querylist.get('function_id')
        user_id = querylist.get('user_id')
        user = User.objects.get(UserID=user_id)
        if function_id == '0':  # My Orders
            orderlist = []
            order = Order.objects.filter(UserID=user_id,Pay=False)
            for x in order:
                y = House.objects.get(HouseID=x.HouseID)
                orderlist.append({
                    'OrderDate':x.OrderDate.date(),
                    'OrderID': x.OrderID,
                    'HouseID': x.HouseID,
                    'LandlordName': y.LandlordName,
                    'LandlordPhone': y.LandlordPhone,
                    'Address': y.Address
                })
            return JsonResponse({'orderlist': orderlist})
        elif function_id == '2':  # My Collection
            houselist = []
            for x in UserHouse.objects.filter(UserID=user_id):
                pics = Picture.objects.filter(HouseID=x.HouseID).values('PicPath')
                house = House.objects.get(HouseID=x.HouseID)
                houselist.append({
                    'HouseID': x.HouseID,
                    'Housename': house.Housename,
                    'Floor':house.Floor,
                    'PicPathList': list(pics),
                    'Address':house.Address,
                    'Area':house.Area,
                    'Housetype':house.Housetype,
                    'Rent':house.Rent,
                })
            return JsonResponse({'houselist': houselist})
        elif function_id == '3':  # Personal Data
            return JsonResponse({'introduction': user.Introduction})
        elif function_id == '4': # Home page
            houselist = []
            allhouse = House.objects.filter()
            for x in allhouse:
                pics = Picture.objects.filter(HouseID=x.HouseID).values('PicPath')
                house = House.objects.get(HouseID=x.HouseID)
                houselist.append({
                    'HouseID': x.HouseID,
                    'Housename': house.Housename,
                    'Floor':house.Floor,
                    'PicPathList': list(pics),
                    'Address': house.Address,
                    'Area': house.Area,
                    'Housetype': house.Housetype,
                    'Rent': house.Rent,
                })
            return JsonResponse({'houselist': houselist})
        elif function_id == '7': #Order details
            order_id = querylist.get('order_id')
            order = Order.objects.get(OrderID=order_id,Pay=True)
            house_id = order.HouseID
            house = House.objects.get(HouseID=house_id)
            return JsonResponse({'Mark':house.Mark,
                                 'HouseID':house.HouseID,
                                 'Housename':house.Housename,
                                 'Rent':house.Rent,
                                 'Housetype': house.Housetype,
                                 'Area': house.Area,
                                 'Floor': house.Floor,
                                 'Type': house.Type,
                                 'LandlordPhone': house.LandlordPhone,
                                 'OrderDate': order.OrderDate.date(),
                                 'DueDate': order.DueDate.date(),
                                 'Introduction': house.Introduction})
    else:
        return JsonResponse({'errornumber': 2, 'message': "Bad request"})

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib import messages
# from .models import *

# # Create your views here.
# def signin(request):
#     signin = House.objects.all()
#     return render(request, 'accounts/first/signin.html', {'signin':signin})

# def homepage(request):
#     return render(request, 'accounts/first/landing.html', {})

# def home(request):
#     return render(request, 'accounts/index.html', {})

# def register(request):
#     if request.method == 'POST':
#         firstName = request.POST['firstName']
#         lastName = request.POST['lastName']
#         sex = request.POST['sex']
#         phoneNum = request.POST['phoneNum']
#         email = request.POST['email']
#         customer_type = request.POST['customer_type']
#         password = request.POST['password']

#         if len(password) >= 8:
#             messages.success('Successfully registered, please login to continue.')
#             return redirect('accounts/first/signin.html')
#         else:

#             newMember = Customer(firstName=firstName, lastName=lastName, sex=sex, phoneNum=phoneNum,
#             email=email, customer_type=customer_type, password=password)
#             newMember.save()

#     return render(request, 'accounts/first/register.html', {})

# def rentals(request):
#     rentals = House.objects.all()
#     return render(request, 'accounts/allHouse.html', {'rentals':rentals})
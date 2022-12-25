from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #signing in possible urls
    path('', views.homepage),

    #homepage possible urls
    path('signin/', views.signin, name='signin'),
    path('login/', views.signin),

    #signing up possible urls
    path('register', views.register, name='register'),
    path('signup/', views.register),
    path('sign-up/', views.register),

    #Full access after register/signin possible urls
    # path('dashboard/', views.dashboard),
    path('rentals/', views.rentals),
    # path('about/', views.about),
    # path('customer/<str:idKey>/', views.customer),
]
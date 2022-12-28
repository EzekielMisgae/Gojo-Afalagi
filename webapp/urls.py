from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings

app_name = 'webapp'

urlpatterns = [
    path('', views.FirstPage, name='FirstPage'),
    path('admin/', admin.site.urls),
    path('FirstPage/', views.FirstPage),
    path('search/',views.search),
    path('order/',views.order),
    path('user/',views.user),
    path('Login/', views.Login),
    path('Register/',views.Register),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.urls import path
# from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#     #signing in possible urls
#     path('', views.homepage, name='landing'),

#     #homepage possible urls
#     path('signin/', views.signin, name='signin'),
#     path('login/', views.signin),

#     #signing up possible urls
#     path('register', views.register, name='register'),
#     path('signup/', views.register),
#     path('sign-up/', views.register),

#     #Full access after register/signin possible urls
#     # path('allhouse/', views.allHouse),
#     path('rentals/', views.rentals),
#     # path('about/', views.about),
#     # path('customer/<str:idKey>/', views.customer),
# ]
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

app_name = 'webapp'

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.landingPage, name='landingPage'),
    path('login',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout',views.logoutUser, name='logout'),

    path('homePage', views.homePage, name='home'),
    path('about',views.about, name='about'),
    path('rentals',views.rentals, name='rentals'),
    path('profile',views.profile, name='profile'),
    path('contact',views.contact, name='contact'),

    path('apartment',views.rentals, name='apartment'),
    path('house',views.rentals, name='house'),
    path('rooms',views.rentals, name='rooms'),
    path('condominium',views.rentals, name='condominium'),
    path('luxurious',views.rentals, name='luxurious'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
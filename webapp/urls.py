from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import house_list, house_detail, house_create


urlpatterns = [

    path('', views.landingPage, name='landingPage'),
    path('login',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout',views.logoutUser, name='logout'),

    path('homePage',views.homePage, name='home'),

    path('about',views.about, name='about'),
    path('aboutme',views.aboutme, name='aboutme'),
    path('profile',views.profile, name='profile'),

    path('<int:pk>/', house_detail, name='house_detail'),
    path('create/', house_create, name='house_create'),

    path('compound',views.compound, name='compound'),
    path('apartment',views.apartment, name='apartment'),
    path('room',views.room, name='room'),
    path('condominium',views.condominium, name='condominium'),
    path('luxurious',views.luxurious, name='luxurious'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
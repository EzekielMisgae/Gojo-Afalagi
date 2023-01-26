from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import house_detail, house_create, search, house_list
from . import decorators


urlpatterns = [

    path('', views.landingPage, name='landingPage'),
    path('login',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout',views.logoutUser, name='logout'),

    path('homePage',views.homePage, name='home'),
    path('unauthorized',decorators.unauthorized, name='unauthorized'),

    path('about',views.about, name='about'),
    path('aboutt',views.aboutt, name='aboutt'),
    path('aboutmee',views.aboutmee, name='aboutmee'),
    path('profile',views.profile, name='profile'),
    path('aboutme',views.aboutme, name='aboutme'),

    path('<int:pk>/', house_detail, name='house_detail'),
    path('create/', house_create, name='house_create'),
    path('house_list/', house_list, name='list'),
    
    path('search/', search, name='search'),
    path('compound',views.compound, name='compound'),
    path('apartment',views.apartment, name='apartment'),
    path('room',views.room, name='room'),
    path('condominium',views.condominium, name='condominium'),
    path('luxurious',views.luxurious, name='luxurious'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
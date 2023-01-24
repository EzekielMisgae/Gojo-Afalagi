from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('', views.landingPage, name='landingPage'),
    path('login',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout',views.logoutUser, name='logout'),

    path('homePage',views.homePage, name='home'),

    path('about',views.about, name='about'),
    path('aboutme',views.aboutme, name='aboutme'),
    path('profile',views.profile, name='profile'),

    path('rentals',views.rentals, name='rentals'),

    path('house',views.house, name='house'),
    path('apartment',views.apartment, name='apartment'),
    path('room',views.room, name='room'),
    path('condominium',views.condominium, name='condominium'),
    path('luxurious',views.luxurious, name='luxurious'),

    # path('create_book/<str:id>/', views.createBook, name="create_book"),
    # path('update_book/<str:id>/', views.updateBook, name="update_book"),
    # path('delete_book/<str:id>/', views.deleteBook, name="delete_book"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
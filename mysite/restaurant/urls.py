# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('chefs/', views.chefs, name='chefs'),
    path('gallery/', views.gallery, name='gallery'),

    # YOUR CUSTOM AUTH VIEWS (these are the ones you actually use)
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
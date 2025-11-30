from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('chefs/', views.chefs_page, name='chefs'),
    path('testimonials/', views.testimonials_page, name='testimonials'),
    path('contact/', views.contact_page, name='contact'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact_form/',views.contact_form,name='contact_form'),
    path('footer/',views.footer,name='footer'),
    path('head/',views.head,name='head'),
    path('home/',views.home,name='home'),
    path('navbar/',views.navbar,name='navbar'),
    path('scripts/',views.scripts,name='scripts'),
]

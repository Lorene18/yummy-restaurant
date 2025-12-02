from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.MenuListView.as_view(), name='list'),
    path('item/<int:pk>/', views.MenuDetailView.as_view(), name='detail'),
    path('add/', views.MenuCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', views.MenuUpdateView.as_view(), name='edit'),
]
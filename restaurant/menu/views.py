from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import MenuItem
from .forms import MenuItemForm
# Create your views here.

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu/list.html'
    context_object_name = 'items'

    def get_queryset(self):
        qs = super().get_queryset().filter(available=True)
        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category)
        return qs

class MenuDetailView(DetailView):
    model = MenuItem
    template_name = 'menu/detail.html'
    context_object_name = 'item'

class MenuCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/form.html'
    success_url = reverse_lazy('menu:list')

class MenuUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/form.html'
    success_url = reverse_lazy('menu:list')
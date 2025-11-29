from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')
def gallery(request):
    return render(request,'gallery.html')
def contact_form(request):
    return render(request,'contact_form.html')
def footer(request):
    return render(request,'footer.html')
def head(request):
    return render(request,' head.html')
def navbar(request):
    return render(request,' navbar.html')
def about(request):
    return render(request, 'about.html')
def scripts(request):
    return render(request,' scripts.html')
def menu(request):
    return render(request, 'menu.html')
def chefs(request):                
    return render(request, 'chefs.html')
def contact(request):              
    return render(request, 'contact.html')
def book_table(request):
    return render(request, 'book_table.html')

def logout(request):
    auth_logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in right after registration
            messages.success(request, f'Welcome {user.username}! Your account has been created.')
            return redirect('accounts:profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')
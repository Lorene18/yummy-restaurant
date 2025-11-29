from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "auth_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "auth_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

def profile_view(request):
    return render(request, "auth_app/profile.html")
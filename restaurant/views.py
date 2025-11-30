from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'restaurant/index.html')
def gallery(request):
    return render(request,'restaurant/gallery.html')
def contact_form(request):
    return render(request,'restaurant/contact_form.html')
def footer(request):
    return render(request,'restaurant/footer.html')
def head(request):
    return render(request,'restaurant/head.html')
def navbar(request):
    return render(request,'restaurant/navbar.html')
def scripts(request):
    return render(request,'restaurant/scripts.html')
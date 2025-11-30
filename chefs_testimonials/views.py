from django.shortcuts import render
from django.http import HttpResponse
from .models import Chef, Testimonial
from .forms import ContactForm


def chefs_page(request):
    chefs = Chef.objects.filter(featured=True)
    return render(request, 'chefs_testimonials/chefs.html', {
        'chefs': chefs
    })

def testimonials_page(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'chefs_testimonials/testimonials.html', {
        'testimonials': testimonials
    })

def contact_page(request):
    return HttpResponse("CONTACT PAGE WORKS")

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save message to the database
            return render(request, 'chefs_testimonials/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'chefs_testimonials/contact.html', {'form': form})
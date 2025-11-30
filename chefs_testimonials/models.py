from django.db import models

class Chef(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='chefs/', blank=True, null=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.name


from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField(default=5)
    approved = models.BooleanField(default=True)  

    def __str__(self):
        return self.name




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return f"Message from {self.name}"

from django.db import models

# Create your models here.
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('dessert','Desserts'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
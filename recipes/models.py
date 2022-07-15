from django.db import models
from fridge.models import Product

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title
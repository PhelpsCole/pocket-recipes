from django.db import models
from products.models import Product

class TextRecipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Recipe(models.Model):
    text = models.ForeignKey(TextRecipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

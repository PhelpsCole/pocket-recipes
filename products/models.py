from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    WEIGHT_CHOICES = [
        ('kg', 'kilogram'),
        ('g', 'gram'),
        ('l', 'litre'),
        ('ml', 'millilitre'),
        ('pc', 'piece'),
        ('tablespoon', 'tablespoon'),
        ('cup', 'cup'),
        ('teaspoon', 'teaspoon'),
        ('ounce', 'ounce')
    ]
    unit_of_measurement = models.TextField(choices=WEIGHT_CHOICES,
                                           blank=False,
                                           default='kg')

    def __str__(self):
        return self.name
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['name', 'unit_of_measurement']

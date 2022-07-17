from django.forms import ModelForm
from .models import Recipe, TextRecipe

class RecipeForm(ModelForm):
    class Meta():
        model = Recipe
        fields = ['text', 'product']

class TextRecipeForm(ModelForm):
    class Meta():
        model = TextRecipe
        fields = ['title', 'description']


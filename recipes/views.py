from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm, TextRecipeForm
from products.forms import ProductForm

def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes':recipes})

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe':recipe})

@login_required
def createrecipe(request):
    if request.method == 'GET':
        return render(request, 'recipes/createrecipe.html',
                      {'product_forms': ProductForm(),
                       'text_form': TextRecipeForm()})
    else:
        option = request.POST.get("add")
        if option == "product":
            return render(request, 'recipes/createrecipe.html',
                          {'product_forms': ProductForm(),
                           'text_form': TextRecipeForm()})
        if option == "text":
            try:
                textrecipe = RecipeForm(request.POST)
                textrecipe.save()
                return render(request, 'recipes/createrecipe.html',
                              {'form': ProductForm()})
            except ValueError:
                return render(request, 'recipes/createrecipe.html',
                              {'form': ProductForm(),
                               'error':'Bad data passed in. Try again.'})

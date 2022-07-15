from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm
from fridge.forms import ProductForm

def recipes(request):
    recipes = Recipe.objects.order_by('title')
    return render(request, 'recipes/home.html', {'recipes':recipes})

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe':recipe})

@login_required
def createrecipe(request):
    if request.method == 'GET':
        return render(request, 'recipes/createrecipe.html',
                      {'form_recipe':RecipeForm(),
                       'form_product':ProductForm()})
    else:
        try:
            if request.POST.get("name"):
                form = ProductForm(request.POST)
                form.save()
                return render(request, 'recipes/createrecipe.html',
                              {'form_recipe':RecipeForm(),
                               'form_product':ProductForm()})
            form = RecipeForm(request.POST)
            newrecipe = form.save(commit=False)
            if newrecipe.title in [f.title for f in Recipe._meta.get_fields()]:
                return render(request, 'recipes/createrecipe.html',
                          {'form_recipe':RecipeForm(),
                           'form_product':ProductForm(),
                           'error':'Enter unique title'})
            newrecipe.save()
            return redirect('recipes:home')
        except ValueError:
            return render(request, 'recipes/createrecipe.html',
                          {'form_recipe':RecipeForm(),
                           'form_product':ProductForm(),
                           'error':'Bad data passed in. Try again.'})


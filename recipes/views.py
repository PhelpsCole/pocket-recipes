from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

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
        ProductFormSet = formset_factory(ProductForm, extra=1)
        return render(request, 'recipes/createrecipe.html',
                      {'product_formset': ProductFormSet,
                       'text_form': TextRecipeForm(),
                       'product_num':1})
    elif request.method == 'POST':
        try:
            product_num = int(request.POST["product_num"])
            ProductFormSet = formset_factory(ProductForm, extra=product_num)
            return render(request, 'recipes/createrecipe.html',
                          {'product_formset': ProductFormSet,
                           'text_form': TextRecipeForm(),
                           'product_num':product_num})
        except:
            pass
    else:
        pass

@login_required
def add(request):
    if request.method == "POST":
        try:
            product_num = int(request.POST["product_num"]) + 1
            ProductFormSet = formset_factory(ProductForm, extra=product_num)
            return render(request, 'recipes/createrecipe.html',
                          {'product_formset': ProductFormSet,
                           'text_form': TextRecipeForm(),
                           'product_num':product_num})
        except:
            pass
    else:
        pass

@login_required
def delete(request):
    if request.method == "POST":
        try:
            product_num = int(request.POST["product_num"]) - 1
            if product_num < 1:
                product_num = 1
            ProductFormSet = formset_factory(ProductForm, extra=product_num)
            return render(request, 'recipes/createrecipe.html',
                          {'product_formset': ProductFormSet,
                           'text_form': TextRecipeForm(),
                           'product_num':product_num})
        except:
            pass
    else:
        pass
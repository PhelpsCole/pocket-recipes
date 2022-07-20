from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

from .models import Recipe
from .forms import RecipeForm, TextRecipeForm
from products.forms import ProductForm

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe':recipe})

@login_required
def recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        return render(request, 'recipes/home.html', {'recipes':recipes})
    elif request.method == 'POST':
        try:
            product_num = int(request.POST["product_num"])
        except:
            pass
        if request.POST.get("option"):
            if request.POST["option"] == "increase":
                product_num += 1
            else:
                product_num -= 1
                if product_num < 1:
                    product_num = 1
        try:
            ProductFormSet = formset_factory(ProductForm, extra=product_num)
            return render(request, 'recipes/createrecipe.html',
                          {'product_formset': ProductFormSet,
                           'text_form': TextRecipeForm(),
                           'product_num':product_num})
        except:
            pass
    else:
        pass
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products':products})

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'products/create.html',
                      {'form': ProductForm()})
    elif request.method == 'POST':
        try:
            product = ProductForm(request.POST)
            product.save()
            return redirect('products:home')
        except ValueError:
            return render(request, 'products/create.html',
                          {'form': ProductForm(),
                           'error':'Bad data passed in. Try again.'})
    else:
        return render(request, 'products/create.html',
                      {'form': ProductForm(),
                       'error':'Incorrect http method. Try again.'})

@login_required
def product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'products/edit.html',
                      {'product':product, 'form':form})
    elif request.method == 'POST':
        if request.POST.get("delete"):
            product.delete()
            return redirect('products:home')
        try:
            print(request.POST)
            product = ProductForm(request.POST, instance=product)
            product.save()
            return redirect('products:home')
        except ValueError:
            return render(request, 'products/edit.html',
                          {'form': ProductForm(),
                           'error':'Bad data passed in. Try again.'})
    else:
        return render(request, 'products/edit.html',
                      {'product':product,
                       'form':form,
                       'error':'Incorrect http method. Try again.'})

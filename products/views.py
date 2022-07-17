from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products':products})

@login_required
def edit(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'products/edit.html', {'product':product, 'form':form})
    else:
        try:
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect('products:home')
        except ValueError:
            return render(request, 'products/edit.html',
                          {'product':product,
                           'form':form,
                           'error':'Bad info. Try again.'})


@login_required
def delete(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:home')

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'products/create.html',
                      {'form': ProductForm()})
    else:
        try:
            product = ProductForm(request.POST)
            product.save()
            return redirect('products:home')
        except ValueError:
            return render(request, 'products/create.html',
                          {'form': ProductForm(),
                           'error':'Bad data passed in. Try again.'})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def fridge(request):
    return render(request, 'fridge/home.html')

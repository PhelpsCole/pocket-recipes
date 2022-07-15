from django.urls import path
from . import views

app_name = 'fridge'

urlpatterns = [
    path('', views.fridge, name='home'),
]
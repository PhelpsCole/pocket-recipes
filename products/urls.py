from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:product_pk>', views.product, name='product'),
    path('create/', views.create, name='create'),
]
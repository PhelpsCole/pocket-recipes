from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:product_pk>', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('create/<int:product_pk>/delete', views.delete, name='delete'),
]
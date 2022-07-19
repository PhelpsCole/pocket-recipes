from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='home'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('create/', views.createrecipe, name='createrecipe'),
    path('create/add', views.add, name='add'),
    path('create/delete', views.delete, name='delete'),
]
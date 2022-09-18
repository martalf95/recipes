from django.urls import path
from list_recipes import views

urlpatterns = [
    path('', views.list_recipes, name="list_recipes"),
    path('/add_recipe', views.add_recipe, name="add_recipe")
]

from django.shortcuts import render

# Create your views here.

def list_recipes(request):
    return render(request, 'list_recipes/list_recipes.html')


def add_recipe(request):
    return render(request, 'list_recipes/add_edit_recipes.html')

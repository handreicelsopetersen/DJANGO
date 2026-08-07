from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe

# Create your views here.
# from django.shortcuts import render

def recipe(request, id:int):
    return render(request, 'receitas/pages/recipe-view.html', context={'name': 'Luiz Otávio', 'recipe': make_recipe(),})

def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Luiz Otávio',
        'recipes': [make_recipe() for _ in range(10)],
    })


def contato(request):
    return render(request, 'receitas/base_template/home.html')

def sobre(request):
    return render(request, 'projeto/base_template/home.html')

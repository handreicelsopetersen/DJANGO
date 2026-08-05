from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.shortcuts import render

def recipe(request,int:id):
    return render(request, 'receitas/pages/home.html', context={'nome': 'receitas'}, status=200)

def home(request):
    return render(request, 'receitas/pages/home.html', context={'nome': 'handrei'}, status=200)


def contato(request):
    return render(request, 'receitas/base_template/home.html')

def sobre(request):
    return render(request, 'projeto/base_template/home.html')

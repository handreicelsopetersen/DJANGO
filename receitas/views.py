from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html', context={'nome': 'handrei'})

def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
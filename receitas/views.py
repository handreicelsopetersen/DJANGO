from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from receitas.views import home


def _home2(request):
    return HttpResponse('HOME1')


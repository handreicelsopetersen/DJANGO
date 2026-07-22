from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home(request):
    return HttpResponse('HOME_urls_teste.py - view')


def contato(request):
    return HttpResponse('contato view')


def sobre(request):
    return HttpResponse('sobre')


def _home(request):
    return HttpResponse('HOME_urls_teste.py 2')


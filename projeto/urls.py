from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.views.generic import RedirectView

def home(request):
    return HttpResponse('HOME')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
]



BKP_urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
    
    path('sobre/', sobre),
    path('contato/', contato),
    path('receitas/', include('receitas.urls')),  # <- aqui mudou: tem prefixo 'receitas/'
    path('sercompe/', RedirectView.as_view(url='https://sercompe.com.br'), name='sercompe'),
]
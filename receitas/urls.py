"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from receitas import views
from django.views.generic import RedirectView
from receitas.views import home, contato, sobre
from. import views



urlpatterns = [
    path('', home, name='Handrei Petersen'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),        
    path('admin/', admin.site.urls),
    path('receitas/', include('receitas.urls')),
    path('', include('receitas.urls')),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre'),
    path('sercompe/', RedirectView.as_view(url='https://sercompe.com.br'), name='sercompe'),
]
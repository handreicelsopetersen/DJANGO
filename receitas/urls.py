from django.urls import path
from receitas.views import home, contato, sobre

from django.views.generic import RedirectView

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
    path('sercompe/', RedirectView.as_view(url='https://sercompe.com.br'), name='sercompe'),
]

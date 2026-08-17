from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from django.urls import path
from receitas import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('contato/', views.contato, name='contato'),
    path('sercompe/', RedirectView.as_view(url='https://sercompe.com.br'), name='sercompe'),
    path('sobre/', views.sobre, name='sobre'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
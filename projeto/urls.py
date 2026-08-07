from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
    path('sercompe/', RedirectView.as_view(url='https://sercompe.com.br'), name='sercompe'),
]
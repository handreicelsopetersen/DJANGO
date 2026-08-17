from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings    
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
    path('sercompe/', RedirectView.as_view(url='https://sercompe.com.br'), name='sercompe'),
]


urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

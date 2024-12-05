from django.urls import path
from .views import UserProfileView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authentication'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    
]

# Asegúrate de añadir esta configuración solo en el entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
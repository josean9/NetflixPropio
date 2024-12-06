from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', profile, name='profile'),  # Página principal del perfil
    path('profile/edit/', UserProfileView.as_view(), name='edit-profile'),  # Editar perfil
]


# Asegúrate de añadir esta configuración solo en el entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
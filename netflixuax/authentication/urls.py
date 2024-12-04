from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserProfileView, EditUserProfileView

app_name = 'authentication'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),  # URL para ver el perfil
    path('profile/edit/', EditUserProfileView.as_view(), name='user-profile-edit'),  # URL para editar perfil
    
]


# Asegúrate de añadir esta configuración solo en el entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
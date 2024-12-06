from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('', profile, name='profile'),  # Página principal del perfil
    path('profile/edit/', EditProfileView.as_view(), name='edit-profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
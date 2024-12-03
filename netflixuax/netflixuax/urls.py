from django.contrib import admin
from django.urls import path, include
from . import views
from authentication.views import UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('streaming.urls')),
    path('auth/', include('authentication.urls')),
  
    path('profile/', UserProfileView.as_view(), name='profile'),

]



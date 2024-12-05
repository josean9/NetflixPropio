from django.urls import path
from .views import UserProfileView
from . import views

app_name = 'authentication'

urlpatterns = [
    
    path('profile/', UserProfileView.as_view(), name='profile'),
]

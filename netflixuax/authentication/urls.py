from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileHTMLView.as_view(), name='profile'),  
    path('profile/rest/', views.UserProfileRestView.as_view(), name='profile-rest'),
]

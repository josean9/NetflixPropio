from django.urls import path
from . import views

app_name = 'snake'

urlpatterns = [
    path('', views.snake_game, name='snake-game'),
]

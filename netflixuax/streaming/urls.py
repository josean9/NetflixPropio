from django.urls import path
from . import views

app_name = 'streaming'
urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('playlist/', views.playlist, name='playlist'),
    path('movies/add_to_playlist/<int:movie_id>/', views.add_to_playlist, name='add-to-playlist'),
    path('series/add_to_playlist/<int:series_id>/', views.add_series_to_playlist, name='add-series-to-playlist'),
    path('series/', views.series, name='series'),  # Nueva ruta para series
    path('api/popular/', views.popular_movies, name='popular-movies'),
    path('api/movie/<int:movie_id>/', views.movie_details, name='movie-details'),
    path('api/movies/', views.MovieListView.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('api/recommendations/', views.RecommendationView.as_view(), name='recommendation'),
]

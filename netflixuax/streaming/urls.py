from . import views
from django.urls import path
from .views import MovieListView, MovieDetailView, PlaylistView, RecommendationView, home
from .views import popular_movies, movie_details

app_name = 'streaming'

"""path('', home, name='home'),"""


urlpatterns = [
    path('', views.home, name='home'),  
    path('movies/', views.movies, name='movies'),
    path('playlist/', views.Playlist, name='playlist'), 


    path('api/popular/', popular_movies, name='popular-movies'),
    path('api/movie/<int:movie_id>/', movie_details, name='movie-details'),
    path('api/movies/', MovieListView.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('api/playlists/', PlaylistView.as_view(), name='playlist'),
    path('api/recommendations/', RecommendationView.as_view(), name='recommendation'),
    
]

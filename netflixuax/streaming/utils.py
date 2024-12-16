import requests
from django.conf import settings
from .models import *
from .scripts.import_movies import *
from .scripts.import_series import *


def fetch_movies_from_tmdb(endpoint, params=None):
    """
    Función genérica para interactuar con la API de TMDb.
    """
    if not params:
        params = {}

    url = f'https://api.themoviedb.org/3/{endpoint}'
    params['api_key'] = settings.TMDB_API_KEY
    params['language'] = 'es-ES'

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error en la API de TMDb: {e}")  # Captura errores de conexión
    

def fetch_and_save_popular_movies(page=1):
    """
    Obtiene películas populares de TMDb y las guarda en la base de datos.
    """
    movies = fetch_popular_movies(page=page)
    for movie_data in movies['results']:
        movie, created = save_movie_to_db(movie_data)
        if created:
            print(f"Added Movie: {movie.title}")
        else:
            print(f"Movie already exists: {movie.title}")


def fetch_and_save_popular_tv_shows(page=1):
    """
    Obtiene series populares de TMDb y las guarda en la base de datos.
    """
    tv_shows = fetch_popular_tv_shows(page=page)
    for tv_data in tv_shows['results']:
        tv_show, created = save_tv_show_to_db(tv_data)
        if created:
            print(f"Added TV Show: {tv_show.title}")
        else:
            print(f"TV Show already exists: {tv_show.title}")



def save_movie_to_db(movie_data):
    """
    Guarda una película en la base de datos.
    """
    movie, created = Movie.objects.get_or_create(
        tmdb_id=movie_data['id'],
        defaults={
            'title': movie_data['title'],
            'description': movie_data['overview'],
            'release_date': movie_data.get('release_date', None),
            'poster_url': f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}" if movie_data.get('poster_path') else None,
            'backdrop_url': f"https://image.tmdb.org/t/p/w500{movie_data['backdrop_path']}" if movie_data.get('backdrop_path') else None,
            'rating': movie_data.get('vote_average', 0),
        }
    )
    return movie, created



def save_tv_show_to_db(tv_data):
    """
    Guarda una serie en la base de datos.
    """
    tv_show, created = Series.objects.get_or_create(
        tmdb_id=tv_data['id'],
        defaults={
            'title': tv_data['name'],
            'description': tv_data['overview'],
            'release_date': tv_data.get('first_air_date', None),
            'poster_url': f"https://image.tmdb.org/t/p/w500{tv_data['poster_path']}" if tv_data.get('poster_path') else None,
            'backdrop_url': f"https://image.tmdb.org/t/p/w500{tv_data['backdrop_path']}" if tv_data.get('backdrop_path') else None,
            'rating': tv_data.get('vote_average', 0),
        }
    )
    return tv_show, created

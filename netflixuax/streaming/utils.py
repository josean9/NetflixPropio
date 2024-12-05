import requests
from django.conf import settings

def fetch_movies_from_tmdb(endpoint, params=None):
    if not params:
        params = {}
    url = f'https://api.themoviedb.org/3/{endpoint}'
    params['api_key'] = settings.TMDB_API_KEY
    params['language'] = 'es-ES'

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en la API de TMDb: {response.status_code} - {response.text}")

def fetch_popular_movies():
    return fetch_movies_from_tmdb('movie/popular')

def fetch_movie_details(movie_id):
    return fetch_movies_from_tmdb(f'movie/{movie_id}')

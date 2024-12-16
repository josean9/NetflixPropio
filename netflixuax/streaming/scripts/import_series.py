import requests
from streaming.models import Series
from django.conf import settings

API_KEY = settings.TMDB_API_KEY

def fetch_and_store_tv_shows(language='en-US', pages=5):
    """
    Importa series populares desde TMDB y las guarda en PostgreSQL.

    Args:
        language (str): Idioma de los datos a recuperar (por defecto: 'en-US').
        pages (int): Número de páginas a importar (por defecto: 5).
    """
    base_url = "https://api.themoviedb.org/3/tv/popular"
    
    for page in range(1, pages + 1):
        params = {
            'api_key': API_KEY,
            'language': language,
            'page': page
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from TMDb: {e}")
            continue
        
        # Procesar los datos de las series
        for tv_data in data.get('results', []):
            try:
                tv_show, created = Series.objects.get_or_create(
                    tmdb_id=tv_data['id'],
                    defaults={
                        'title': tv_data.get('name', 'No Title'),
                        'description': tv_data.get('overview', 'No Description'),
                        'release_date': tv_data.get('first_air_date', None),
                        'poster_url': (
                            f"https://image.tmdb.org/t/p/w500{tv_data['poster_path']}"
                            if tv_data.get('poster_path') else None
                        ),
                        'backdrop_url': (
                            f"https://image.tmdb.org/t/p/w500{tv_data['backdrop_path']}"
                            if tv_data.get('backdrop_path') else None
                        ),
                        'rating': tv_data.get('vote_average', 0),
                    }
                )
                if created:
                    print(f"Added TV Show: {tv_show.title}")
                else:
                    print(f"TV Show already exists: {tv_show.title}")
            except Exception as e:
                print(f"Error saving TV Show {tv_data.get('name', 'Unknown')}: {e}")

import requests
from streaming.models import Series

API_KEY = "b1c4ff670df4325eb0457288933bd696"

def fetch_and_store_tv_shows():
    """
    Importa 100 series de televisión populares desde TMDB a la base de datos.
    """
    for page in range(1, 6):  # 5 páginas
        url = f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for tv_data in data['results']:
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
                if created:
                    print(f"Added TV Show: {tv_show.title}")
        else:
            print(f"Failed to fetch data from TMDb. Status code: {response.status_code}")

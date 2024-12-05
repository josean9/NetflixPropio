from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer, PlaylistSerializer, RecommendationSerializer
from django.http import JsonResponse
from .utils import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Playlist, Recommendation, Series

@login_required
def add_to_playlist(request, movie_id):
    playlist, _ = Playlist.objects.get_or_create(user=request.user, name="My Playlist")
    movie = get_object_or_404(Movie, id=movie_id)

    if movie in playlist.movies.all():
        playlist.movies.remove(movie)
    else:
        playlist.movies.add(movie)

    return redirect('streaming:movies')

@login_required
def add_series_to_playlist(request, series_id):
    playlist, _ = Playlist.objects.get_or_create(user=request.user, name="My Playlist")
    tv_show = get_object_or_404(Series, id=series_id)

    if tv_show in playlist.series.all():
        playlist.series.remove(tv_show)
    else:
        playlist.series.add(tv_show)

    return redirect('streaming:series')  # Redirige de vuelta a la lista de series


@login_required
def playlist(request):
    playlist, _ = Playlist.objects.get_or_create(user=request.user, name="My Playlist")
    return render(request, 'streaming/playlist.html', {'playlist': playlist})

from itertools import chain

def home(request):
    """
    Vista de inicio que mezcla películas y series.
    """
    movies = Movie.objects.all()
    tv_shows = Series.objects.all()

    # Agregar un campo 'content_type' a cada elemento
    for movie in movies:
        movie.content_type = "Película"
    for tv_show in tv_shows:
        tv_show.content_type = "Serie"

    # Mezclar películas y series
    mixed_content = sorted(
        chain(movies, tv_shows),
        key=lambda x: x.release_date if x.release_date else ""
    )
    return render(request, 'streaming/home.html', {'mixed_content': mixed_content})


def movies(request):
    movies_list = Movie.objects.all()
    return render(request, 'streaming/movies.html', {'movies': movies_list})


def series(request):
    """
    Muestra todas las series en un HTML.
    """
    tv_shows = Series.objects.all()
    return render(request, 'streaming/series.html', {'tv_shows': tv_shows})


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)


class PlaylistView(APIView):
    def get(self, request):
        playlists = Playlist.objects.filter(user=request.user)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        playlist = Playlist.objects.create(name=data['name'], user=request.user)
        if 'movies' in data:
            for movie_id in data['movies']:
                movie = Movie.objects.get(id=movie_id)
                playlist.movies.add(movie)
        playlist.save()
        return Response(PlaylistSerializer(playlist).data, status=status.HTTP_201_CREATED)


class RecommendationView(APIView):
    def get(self, request):
        try:
            recommendation = Recommendation.objects.get(user=request.user)
            serializer = RecommendationSerializer(recommendation)
            return Response(serializer.data)
        except Recommendation.DoesNotExist:
            return Response({"message": "No recommendations found."}, status=status.HTTP_404_NOT_FOUND)


def popular_movies(request):
    try:
        data = fetch_popular_movies()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def movie_details(request, movie_id):
    try:
        data = fetch_movie_details(movie_id)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def populate_series():
    """
    Poblar la base de datos con series populares desde TMDB.
    """
    try:
        data = fetch_popular_tv_shows()
        for series_data in data['results']:
            Series.objects.get_or_create(
                tmdb_id=series_data['id'],
                defaults={
                    'title': series_data['name'],
                    'description': series_data['overview'],
                    'release_date': series_data.get('first_air_date', None),
                    'poster_url': f"https://image.tmdb.org/t/p/w500{series_data['poster_path']}" if series_data.get('poster_path') else None,
                    'backdrop_url': f"https://image.tmdb.org/t/p/w500{series_data['backdrop_path']}" if series_data.get('backdrop_path') else None,
                    'rating': series_data.get('vote_average', 0),
                }
            )
    except Exception as e:
        print(f"Error populating series: {str(e)}")

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()
    backdrop_url = models.URLField()
    tmdb_id = models.IntegerField(unique=True)
    genre = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.title
    
   

class Series(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    backdrop_url = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    movies = models.ManyToManyField(Movie, related_name='playlists')
    series = models.ManyToManyField(Series, related_name='playlists')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Recommendation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recommendation')
    recommended_movies = models.ManyToManyField(Movie, related_name='recommendations')

    def __str__(self):
        return f"Recommendations for {self.user.username}"

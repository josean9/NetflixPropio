from django.contrib import admin
from .models import Movie, Playlist, Recommendation

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Movie)
admin.site.register(Playlist)
admin.site.register(Recommendation)

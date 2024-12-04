from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserSerializer
from django.core.exceptions import ValidationError


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request):
        """Obtiene los detalles del perfil del usuario autenticado"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        """Actualiza el perfil del usuario autenticado"""
        user = request.user
        data = request.data
        profile = user.profile

        # Actualizar biografía
        profile.bio = data.get('bio', profile.bio)

        # Actualizar fecha de nacimiento
        birth_date = data.get('birth_date', None)
        if birth_date:
            try:
                profile.birth_date = birth_date
            except ValueError:
                return Response({"error": "Fecha de nacimiento inválida."}, status=status.HTTP_400_BAD_REQUEST)

        # Actualizar avatar
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']

        # Guardar cambios
        profile.save()

        # Serializar y devolver los datos actualizados
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        """Permite al usuario editar su perfil."""
        user = request.user
        data = request.data
        profile = user.profile

        # Cambiar la biografía si se proporciona
        profile.bio = data.get('bio', profile.bio)

        # Cambiar la fecha de nacimiento si se proporciona
        profile.birth_date = data.get('birth_date', profile.birth_date)

        # Si el usuario sube un avatar, lo actualiza
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']

        # Guardar los cambios en el perfil
        profile.save()

        # Serializar los datos del usuario y devolver la respuesta
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

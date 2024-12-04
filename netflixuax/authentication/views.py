from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def put(self, request):
        """Actualiza el perfil del usuario autenticado"""
        user = request.user
        data = request.data
        profile = user.profile
        profile.bio = data.get('bio', profile.bio)
        profile.birth_date = data.get('birth_date', profile.birth_date)
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get(self, request):
        """Obtiene los detalles del perfil del usuario autenticado"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    
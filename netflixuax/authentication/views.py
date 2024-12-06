from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import UserProfile
from .forms import UserProfileForm  # Asegúrate de crear un formulario

@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    """Vista para editar el perfil del usuario"""
    def get(self, request):
        user = request.user
        try:
            profile = user.profile
        except UserProfile.DoesNotExist:
            profile = None  # Caso donde no hay perfil aún

        form = UserProfileForm(instance=profile)
        return render(request, 'authentication/edit_profile.html', {'form': form})

    def post(self, request):
        user = request.user
        try:
            profile = user.profile
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=user)

        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('authentication:profile')
        return render(request, 'authentication/edit_profile.html', {'form': form})


@login_required
def profile(request):
    """Muestra el perfil del usuario autenticado."""
    user = request.user
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        profile = None  # Si el perfil no existe, maneja este caso

    return render(request, 'authentication/profile.html', {'profile': profile})




class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def put(self, request):
        """Actualiza el perfil del usuario autenticado"""
        user = request.user
        data = request.data
        profile = user.profile
        profile.bio = data.get('bio', profile.bio)
        profile.birth_date = data.get('birth_date', profile.birth_date)
        """if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']"""
        profile.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get(self, request):
        """Obtiene los detalles del perfil del usuario autenticado"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """Formulario para editar el perfil del usuario"""
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'birth_date']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

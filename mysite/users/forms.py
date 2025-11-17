from django import forms
from users.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'description']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Введите описание'
            }),
        }
        # labels = {
        #     'profile_picture': 'Фото профиля',
        #     'description': 'Описание'
        # }

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
    )

    class Meta:
        model = Message
        fields = ['content']

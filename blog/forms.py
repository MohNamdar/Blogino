from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام شما'}),
            'message': forms.Textarea(attrs={'placeholder': 'متن کامنت شما'}),
            'email': forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
        }

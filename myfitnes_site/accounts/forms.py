from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.validators import FileExtensionValidator

import uuid
from datetime import timedelta
from .models import EmailVerification
from django.utils import timezone

User = get_user_model()


class UserRegistrationsForm(forms.ModelForm)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    
    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                '"A user with such an email already exists")'
            )
        return email
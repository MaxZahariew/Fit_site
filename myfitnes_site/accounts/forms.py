from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.validators import FileExtensionValidator

import uuid
from datetime import timedelta
from .models import EmailVerification, User
from django.utils import timezone

# User = get_user_model()


class UserRegistrationsForm(forms.ModelForm):
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

    def clean_password2(self):
        cd = self.cleaned_data
        if 'password' in cd and 'password2' in cd:
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Пароли не совпадают')
        else:
            raise forms.ValidationError('Пожалуйста, заполните оба поля пароля.')

        return cd['password2']

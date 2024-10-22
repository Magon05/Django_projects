from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CreateForm(forms.ModelForm):
    fullname = forms.CharField(max_length=200)
    phonenumber = forms.CharField(max_length=200)
    phonetype = forms.CharField(max_length=200)
    comment = forms.CharField(max_length=200)


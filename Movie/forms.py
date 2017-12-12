from .models import *
from django import forms
from django.contrib.auth.models import User

class UserFrom(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Enter username'}
    ),required=True, max_length=30)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email'}
    ), required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ), required=True, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}
    ), required=True, min_length=8)

    class Meta():
        model = User
        fields = ['username', 'email', 'password']
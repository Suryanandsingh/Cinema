from .models import *
from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User

class UserFrom(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Enter username'}
    ),required=True, max_length=20)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name'}
    ), required=True, max_length=30)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email'}
    ), required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ), required=True, min_length=8)

    class Meta():
        model = User
        fields = ['username', 'first_name', 'email', 'password']

    #validation of unique email
    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        try:
            check_email = validate_email(email)
        except:
            raise forms.ValidationError("Email is not correct format")
        return email


from django import forms
from django.contrib.auth.models import User
from .models import *

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email...'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your frist name...'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your last name...'}))
    password_1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'password...'}))
    password_2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'password...'}))

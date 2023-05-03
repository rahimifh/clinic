from django import forms
#*********002
from django.contrib.auth.models import User
#*******003
from .models import Profile
#****


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

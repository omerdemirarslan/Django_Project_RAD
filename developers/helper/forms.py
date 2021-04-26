import logging

from django import forms
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from developers.models import DeveloperUser


class RegistrationForms(forms.Form):
    """
    This Class Create Form For The Registration Process
    """
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

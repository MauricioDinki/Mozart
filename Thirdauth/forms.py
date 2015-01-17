# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .validations import *

class LoginForm(forms.Form):

    username = forms.CharField(
    	widget=forms.TextInput(attrs={'placeholder':'username'}),
    )

    password = forms.CharField(
    	widget=forms.PasswordInput(attrs={'placeholder':'password'}),
    )

    def clean_username(self):
		username = self.cleaned_data.get('username')
		validate_null(username)
		return username

    def clean_password(self):
		password = self.cleaned_data.get('password')
		validate_null(password)
		return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(custom_error_messages['invalid_login'],)
            elif not self.user_cache.is_active:
                raise forms.ValidationError(custom_error_messages['inactive'])
        return self.cleaned_data

class RegisterForm(forms.Form):
    # TODO: Define form fields here
    

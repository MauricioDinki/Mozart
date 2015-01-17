# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .validations import *
from Profiles.models import days,months

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

    email = forms.EmailField(
        max_length=20,
        required=True,
    )

    last_name = forms.CharField(
        max_length=20,
        required=True,
    )

    name = forms.CharField(
        max_length=20,
        required=True,
    )

    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(),
    )

    username = forms.CharField(
        max_length=20,
        required=True,
    )

    day_of_birth = forms.ChoiceField(
        required=True,
        choices=days,
    )

    month_of_birth = forms.ChoiceField(
        required=True,
        choices=months,
    )

    year_of_birth = forms.IntegerField(
        required=True,
        max_value=2015,
        min_value=1905,
    )









    

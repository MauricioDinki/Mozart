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

    day_of_birth = forms.ChoiceField(
        error_messages=default_error_messages,
        required=True,
        choices=days,
    )

    email = forms.EmailField(
        error_messages={
            'invalid':('Ingresa una cuenta de correo valida'),
            'required': default_error_messages['required']
        },
        max_length=30,
        required=True,
    )

    last_name = forms.CharField(
        error_messages=default_error_messages,
        max_length=30,
        required=True,
    )

    name = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
    )

    month_of_birth = forms.ChoiceField(
        error_messages=default_error_messages,
        required=True,
        choices=months,
    )

    password_1 = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
        widget=forms.PasswordInput(),
    )

    password_2 = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
        widget=forms.PasswordInput(),
    )

    username = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
    )

    year_of_birth = forms.IntegerField(
        error_messages=default_error_messages,
        required=True,
        max_value=2015,
        min_value=1905,
    )

    def clean_day_of_birth(self):
        day_of_birth = self.cleaned_data.get('day_of_birth')
        validate_null(day_of_birth)
        return day_of_birth

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email(email)
        return email

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        validate_null(last_name)
        return last_name

    def clean_name(self):
        name = self.cleaned_data.get('name')
        validate_null(name)
        return name

    def clean_month_of_birth(self):
        month_of_birth = self.cleaned_data.get('month_of_birth')
        validate_null(month_of_birth)
        return month_of_birth

    def clean_password_1(self):
        password_1 = self.cleaned_data.get('password_1')
        validate_null(password_1)
        return password_1

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get("password_2")
        validate_password(password_1,password_2)
        return password_1 and password_2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        validate_username(username)
        return username

    def clean_year_of_birth(self):
        year_of_birth = self.cleaned_data.get('year_of_birth')
        validate_null(year_of_birth)
        return year_of_birth

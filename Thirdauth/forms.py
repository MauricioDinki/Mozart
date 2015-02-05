# -*- encoding: utf-8 -*-

from .validations import *
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth

class LoginForm(forms.Form):

    username = forms.CharField(
        error_messages=default_error_messages,
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Username'}),
    )

    password = forms.CharField(
        error_messages=default_error_messages,
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'Password'}),
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

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
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=days,
        widget=forms.Select(attrs={'class' : 'form-control',}),
    )

    email = forms.EmailField(
        error_messages={
            'invalid':('Ingresa una cuenta de correo valida'),
            'required': default_error_messages['required']
        },
        max_length=30,
        required=True,
        widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'Email'}),

    )

    month_of_birth = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=months,
        widget=forms.Select(attrs={'class' : 'form-control',}),
    )

    password_1 = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Password'}),
    )

    password_2 = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Confirmar Password'}),
    )

    type_of_user = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=type_of_users,
        widget=forms.Select(attrs={'class' : 'form-control',}),
    )

    username = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Username'}),
    )

    year_of_birth = forms.IntegerField(
        error_messages=default_error_messages,
        required=True,
        max_value=2015,
        min_value=1905,
        widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'Año'}),
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean_day_of_birth(self):
        day_of_birth = self.cleaned_data.get('day_of_birth')
        validate_null(day_of_birth)
        return day_of_birth

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email(email)
        return email

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

    def clean_type_of_user(self):
        type_of_user = self.cleaned_data.get('type_of_user')
        validate_null(type_of_user)
        return type_of_user

    def clean_username(self):
        username = self.cleaned_data.get('username')
        validate_username(username)
        return username

    def clean_year_of_birth(self):
        year_of_birth = self.cleaned_data.get('year_of_birth')
        validate_null(year_of_birth)
        return year_of_birth

    def save(self):
        day_of_birth = self.cleaned_data.get('day_of_birth')
        email = self.cleaned_data.get('email')
        month_of_birth = self.cleaned_data.get('month_of_birth')
        password = self.cleaned_data.get("password_2")
        type_of_user = self.cleaned_data.get('type_of_user')
        username = self.cleaned_data.get('username')
        year_of_birth = self.cleaned_data.get('year_of_birth')

        user = User.objects.create_user(username,email,password)

        newExtendedUser = Mozart_User(user=user,user_type=type_of_user)
        newExtendedUser.save()

        newUserAge = Date_of_Birth(user=user,day=day_of_birth,month=month_of_birth,year=year_of_birth)
        newUserAge.save()

        self.user_cache = authenticate(username=username, password=password)
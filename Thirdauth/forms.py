# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .validations import *
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth

class LoginForm(forms.Form):

    username = forms.CharField(
        error_messages=default_error_messages,
        max_length=30,
        required=True,
    )

    password = forms.CharField(
        error_messages=default_error_messages,
        max_length=30,
        required=True,
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
                raise forms.ValidationError(custom_error_messages['invalid_choice_login'],)
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
    )

    email = forms.EmailField(
        error_messages={
            'invalid':('Ingresa una cuenta de correo valida'),
            'required': default_error_messages['required']
        },
        max_length=30,
        required=True,
    )

    first_name = forms.CharField(
        error_messages=default_error_messages,
        max_length=20,
        required=True,
    )

    last_name = forms.CharField(
        error_messages=default_error_messages,
        max_length=30,
        required=True,
    )


    month_of_birth = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
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

    sexuality = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=sexuality
    )

    type_of_user = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=type_of_users,
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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        validate_null(first_name)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        validate_null(last_name)
        return last_name

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

    def clean_sexuality(self):
        sexuality = self.cleaned_data.get('sexuality')
        validate_null(sexuality)
        return sexuality

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
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        month_of_birth = self.cleaned_data.get('month_of_birth')
        password = self.cleaned_data.get("password_2")
        sexuality = self.cleaned_data.get("sexuality")
        type_of_user = self.cleaned_data.get('type_of_user')
        username = self.cleaned_data.get('username')
        year_of_birth = self.cleaned_data.get('year_of_birth')

        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        newExtendedUser = Mozart_User(user=user,sex=sexuality,user_type=type_of_user)
        newExtendedUser.save()

        newUserAge = Date_of_Birth(user=user,day=day_of_birth,month=month_of_birth,year=year_of_birth)
        newUserAge.save()

        self.user_cache = authenticate(username=username, password=password)
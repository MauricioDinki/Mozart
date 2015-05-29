# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import six

from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from datetime import date
from Profiles.models import days, months, type_of_users, sexuality, Mozart_User, Date_of_Birth, Address, Contact
from Utils.messages import default_messages, custom_messages
from Utils.validators import eval_iexact, eval_matching, eval_blank


class LoginForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_name = 'loginform'

    username = forms.CharField(
        max_length=20,
        min_length=5,
        validators=[RegexValidator(regex=u'^[a-zA-Z0-9]*$')],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Escribe tu nickname',
                'mz-field': '',
            }
        ),
    )

    password = forms.CharField(
        max_length=40,
        min_length=6,
        validators=[eval_blank],
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Escribe tu contraseña',
                'mz-field': '',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].required = True

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(custom_messages['invalid_login'],)
            elif not self.user_cache.is_active:
                raise forms.ValidationError(custom_messages['inactive_account'])
        return self.cleaned_data


class RegisterForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'signupFormCtrl'
    form_name = 'signupform'
    this_year = date.today().year

    day_of_birth = forms.ChoiceField(
        choices=days,
        initial='1',
        widget=forms.Select(
            attrs={
                'class': 'mozart-field active-field',
                'ng-change': 'validateDate()',
                'mz-field': '',
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Escribe tu email',
                'mz-field': '',
            }
        ),
    )

    month_of_birth = forms.ChoiceField(
        choices=months,
        initial='Enero',
        widget=forms.Select(
            attrs={
                'class': 'mozart-field active-field',
                'ng-change': 'validateDate()',
                'mz-field': '',
            }
        ),
    )

    password_1 = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Elije una contraseña',
                'mz-field': '',
            }
        ),
    )

    password_2 = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Vuelve a escribir tu contraseña',
                'mz-field': '',
                'mz-match': 'password_1',
            }
        ),
    )

    type_of_user = forms.ChoiceField(
        choices=type_of_users,
        widget=forms.Select(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    username = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Escribe tu nickname',
                'mz-field': '',
            }
        ),
    )

    year_of_birth = forms.IntegerField(
        max_value=this_year - 18,
        min_value=this_year - 100,
        widget=forms.NumberInput(
            attrs={
                'class': 'mozart-field active-field',
                'placeholder': 'Año',
                'ng-change': 'validateDate()',
                'value':  this_year - 25,
                'mz-field': '',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].validators = [RegexValidator(regex=u'^[a-zA-Z0-9]*$',), ]
            if field == 'email':
                self.fields[field].validators = [RegexValidator(regex=u'^[\w.@+-]+$',), ]
            if field == 'username':
                self.fields[field].validators = [RegexValidator(regex=u'^[a-zA-Z0-9]*$')]
            self.fields[field].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return eval_iexact(email, User, 'email')

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        return eval_matching(password_1, password_2)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return eval_iexact(username, User, 'username')

    def save(self):
        cleaned_data = super(RegisterForm, self).clean()

        user = User.objects.create_user(username, email, password)

        newExtendedUser = Mozart_User(
            user=user,
            user_type=cleaned_data.get('type_of_user')
        )

        newExtendedUser.nationality = 'MX'
        newExtendedUser.save()

        newUserAge = Date_of_Birth(
            user=user,
            day=cleaned_data.get('day_of_birth'),
            month=cleaned_data.get('month_of_birth'),
            year=cleaned_data.get('year_of_birth')
        )

        newUserAge.save()

        newUserContact = Contact(user=user)
        newUserContact.save()

        newUserAddress = Address(user=user)
        newUserAddress.save()

        self.user_cache = authenticate(
            username=cleaned_data.get('username'),
            password=cleaned_data.get("password_2")
        )

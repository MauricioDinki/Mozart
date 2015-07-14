#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.utils import six
from django.contrib.auth.models import User

from django_countries import countries
from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from mozart.core import validators
from mozart.core.messages import regex_sentences, custom_error_messages


class ChangePasswordForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_name = 'passwordform'

    old_password = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    new_password_1 = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    new_password_2 = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'mz-match': 'new_password_1',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [validators.eval_blank]
            self.fields[field].required = True

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        username = self.request.user.username
        return validators.eval_password(username, password)

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        new_password_1 = cleaned_data.get('new_password_1')
        new_password_2 = cleaned_data.get('new_password_2')
        if new_password_1 and new_password_2:
            return validators.eval_matching(new_password_1, new_password_2)
        return cleaned_data

    def save(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        user_instance = self.request.user
        user_instance.set_password(cleaned_data.get('new_password_2'))
        user_instance.save()


class ProfileForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'editInformationCtrl'
    form_name = 'informationform'

    username = forms.CharField(
        min_length=5,
        max_length=20,
        required=True,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9]*$/',
            }
        ),
    )

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters_special'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z_áéíóúñ\s]*$/',
            }
        ),
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters_special'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z_áéíóúñ\s]*$/',
            }
        ),
    )

    profile_picture = forms.ImageField(
        required=False,
        validators=[validators.eval_image],
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
                'file-upload': '',
                'file-bind': 'profilePicture',
                'mz-field': ''
            }
        ),
    )

    nationality = forms.ChoiceField(
        choices=countries,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters_special'])],
        widget=forms.Select(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ\s]*$/',
            }
        ),
    )

    description = forms.CharField(
        max_length=200,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters_special'])],
        widget=forms.Textarea(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z_áéíóúñ\s]*$/',
            }
        ),
    )

    personal_homepage = forms.URLField(
        required=False,
        validators=[validators.eval_blank],
        widget=forms.URLInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': ''
            }
        ),
    )

    phone_number = forms.IntegerField(
        required=False,
        max_value=9999999999,
        min_value=0,
        validators=[validators.eval_blank],
        widget=forms.NumberInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    address = forms.CharField(
        min_length=10,
        max_length=100,
        required=False,
        validators=[validators.eval_blank],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ#\s]*$/',
            }
        ),
    )

    city = forms.CharField(
        min_length=5,
        max_length=30,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters_special'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ\s]*$/',
            }
        ),
    )

    zip_code = forms.CharField(
        min_length=5,
        max_length=10,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['zip_code'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[0-9\-]*$/',
            }
        ),
    )

    neighborhood = forms.CharField(
        min_length=4,
        max_length=200,
        required=False,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters_special'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ\s]*$/',
            }
        ),
    )

    password = forms.CharField(
        min_length=6,
        max_length=40,
        required=True,
        validators=[validators.eval_blank],
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': ''
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.same_username = False
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.lower() == self.request.user.username.lower():
            self.same_username = True
            return username
        else:
            self.same_username = False
            try:
                User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                return username
            else:
                raise forms.ValidationError(
                    custom_error_messages['unique'],
                    params={
                        'model_name': User._meta.verbose_name.lower(),
                        'field_label': User._meta.get_field('username').verbose_name.lower()
                    }
                )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.request.user.username
        return validators.eval_password(username, password)

    def save(self):
        cleaned_data = super(ProfileForm, self).clean()
        same_username = self.same_username
        user_instance = self.request.user

        if not same_username:
            user_instance.username = cleaned_data.get('username')

        user_instance.first_name = cleaned_data.get('first_name')
        user_instance.last_name = cleaned_data.get('last_name')
        user_instance.save()

        user_instance.extendeduser.nationality = cleaned_data.get('nationality')
        user_instance.extendeduser.description = cleaned_data.get('description')

        if self.request.FILES.get('profile_picture', False):
            user_instance.extendeduser.profile_picture = self.request.FILES['profile_picture']

        user_instance.extendeduser.save()

        user_instance.contact.personal_homepage = cleaned_data.get('personal_homepage')
        user_instance.contact.phone_number = cleaned_data.get('phone_number')
        user_instance.contact.save()

        user_instance.address.address = cleaned_data.get('address')
        user_instance.address.city = cleaned_data.get('city')
        user_instance.address.zip_code = cleaned_data.get('zip_code')
        user_instance.address.neighborhood = cleaned_data.get('neighborhood')
        user_instance.address.save()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.utils import six
from django.contrib.auth.models import User

from django_countries import countries
from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from mozart.core import validators
from mozart.core.messages import regex_sentences, custom_error_messages


# class PasswordUpdateForm(forms.Form):
class PasswordUpdateForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
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
        super(PasswordUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [validators.eval_blank]
            self.fields[field].required = True

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        username = self.request.user.username
        return validators.eval_password(username, password)

    def clean(self):
        cleaned_data = super(PasswordUpdateForm, self).clean()
        new_password_1 = cleaned_data.get('new_password_1')
        new_password_2 = cleaned_data.get('new_password_2')
        if new_password_1 and new_password_2:
            return validators.eval_matching(new_password_1, new_password_2)
        return cleaned_data

    def save(self):
        cleaned_data = super(PasswordUpdateForm, self).clean()
        print cleaned_data
        user_instance = self.request.user
        user_instance.set_password(cleaned_data.get('new_password_2'))
        user_instance.save()


# class ProfileForm(forms.Form):
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
                        User._meta.verbose_name.lower(),
                        User._meta.get_field('username').verbose_name.lower()
                    }
                )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.request.user.username
        return validators.eval_password(username, password)

    def save(self):
        same_username = self.same_username
        user_insta = self.request.user

        if not same_username:
            user_insta.username = self.cleaned_data.get('username')

        user_insta.first_name = self.cleaned_data.get('first_name')
        user_insta.last_name = self.cleaned_data.get('last_name')
        user_insta.save()

        user_insta.extendeduser.nationality = self.cleaned_data.get('nationality')
        user_insta.extendeduser.description = self.cleaned_data.get('description')

        if self.request.FILES.get('profile_picture', False):
            user_insta.extendeduser.profile_picture = self.request.FILES['profile_picture']

        user_insta.extendeduser.save()

        user_insta.contact.personal_homepage = self.cleaned_data.get('personal_homepage')
        user_insta.contact.phone_number = self.cleaned_data.get('phone_number')
        user_insta.contact.save()

        user_insta.address.address = self.cleaned_data.get('address')
        user_insta.address.city = self.cleaned_data.get('city')
        user_insta.address.zip_code = self.cleaned_data.get('zip_code')
        user_insta.address.neighborhood = self.cleaned_data.get('neighborhood')
        user_insta.address.save()

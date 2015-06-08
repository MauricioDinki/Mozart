# -*- encoding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.utils import six

from django_countries import countries
from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin
from djangular.forms import NgModelFormMixin, NgFormValidationMixin

from Profiles.models import Mozart_User
from Utils.messages import default_messages
from Utils.validators import eval_image, eval_blank, eval_password, eval_matching


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
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].validators = [eval_blank]
            self.fields[field].required = True

    def clean_new_password_2(self):
        new_password_1 = self.cleaned_data.get('new_password_1')
        new_password_2 = self.cleaned_data.get('new_password_2')
        return eval_matching(new_password_1, new_password_2)

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        username = self.request.user.username
        return eval_password(username, password)

    def save(self):
        user_to_change = self.request.user
        user_to_change.set_password(self.cleaned_data.get('new_password_2'))
        user_to_change.save()


class UserInformationForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'editInformationCtrl'
    form_name = 'informationform'

    username = forms.CharField(
        min_length=5,
        max_length=20,
        required=True,
        validators=[RegexValidator(regex=u'^[a-zA-Z0-9]*$')],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_ñÑ]*$/',
            }
        ),
    )

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        required=False,
        validators=[RegexValidator(regex=u'^[a-zA-Z_áéíóúñ\s]*$')],
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
        validators=[RegexValidator(regex=u'^[a-zA-Z_áéíóúñ\s]*$')],
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
        validators=[eval_image],
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
        validators=[RegexValidator(regex=u'^[a-zA-Z_áéíóúñ\s]*$')],
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
        validators=[RegexValidator(regex=u'^[a-zA-Z_áéíóúñ\s]*$')],
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
        validators=[eval_blank],
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
        validators=[eval_blank],
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
        validators=[RegexValidator(regex=u'^[a-zA-Z0-9_áéíóúñ#\s]*$')],
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
        validators=[RegexValidator(regex=u'^[a-zA-Z_áéíóúñ\s]*$')],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ#\s]*$/',
            }
        ),
    )

    zip_code = forms.CharField(
        min_length=5,
        max_length=10,
        required=False,
        validators=[RegexValidator(regex=u'^[0-9\-]*$')],
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
        validators=[RegexValidator(regex=u'^[a-zA-Z_áéíóúñ\s]*$')],
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
        validators=[eval_blank],
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
        super(UserInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.lower() == self.request.user.username.lower():
            self.same_username = True
            return username
        else:
            self.same_username = False
            try:
                user = User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                return username
            else:
                raise forms.ValidationError(default_messages['unique'])

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.request.user.username
        return eval_password(username, password)

    def save(self):
        same_username = self.same_username
        user_to_change = self.request.user

        if not same_username:
            user_to_change.username = self.cleaned_data.get('username')

        user_to_change.first_name = self.cleaned_data.get('first_name')
        user_to_change.last_name = self.cleaned_data.get('last_name')
        user_to_change.save()

        user_to_change.mozart_user.nationality = self.cleaned_data.get('nationality')
        user_to_change.mozart_user.description = self.cleaned_data.get('description')

        if self.request.FILES.get('profile_picture', False):
            user_to_change.mozart_user.profile_picture = self.request.FILES['profile_picture']

        user_to_change.mozart_user.save()

        user_to_change.contact.personal_homepage = self.cleaned_data.get('personal_homepage')
        user_to_change.contact.phone_number = self.cleaned_data.get('phone_number')
        user_to_change.contact.save()

        user_to_change.address.address = self.cleaned_data.get('address')
        user_to_change.address.city = self.cleaned_data.get('city')
        user_to_change.address.zip_code = self.cleaned_data.get('zip_code')
        user_to_change.address.neighborhood = self.cleaned_data.get('neighborhood')
        user_to_change.address.save()

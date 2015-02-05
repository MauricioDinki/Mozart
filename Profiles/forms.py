from .models import Mozart_User
from django import forms
from django.contrib.auth import authenticate
from django_countries import countries
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth
from Thirdauth.forms import RegisterForm
from Thirdauth.validations import *

class UserInformationForm(forms.Form):

	username = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
	)

	first_name = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
	)

	last_name = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
	)
	
	nationality = forms.ChoiceField(
		choices=countries,
		error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
		required=True,
	)

	description = forms.CharField(
		error_messages=default_error_messages,
		max_length=200,
		required=True,
		widget=forms.Textarea()
	)

	personal_homepage = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	phone_number = forms.IntegerField(
		error_messages=default_error_messages,
		required=True,
	)

	password = forms.CharField(
	    error_messages=default_error_messages,
	    max_length=20,
	    required=True,
	    widget=forms.PasswordInput(),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.user_cache = None
		super(UserInformationForm, self).__init__(*args, **kwargs)


	def clean_username(self):
		username = self.cleaned_data.get('username')
		validate_null(username)
		return username

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		validate_null(first_name)
		return first_name

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		validate_null(last_name)
		return last_name

	def clean_nationality(self):
		nationality = self.cleaned_data.get('nationality')
		validate_null(nationality)
		return validate_null

	def clean_description(self):
		description = self.cleaned_data.get('description')
		validate_null(description)
		return description

	def clean_personal_homepage(self):
		personal_homepage = self.cleaned_data.get('personal_homepage')
		validate_null(personal_homepage)
		return personal_homepage

	def cleaned_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		validate_null(phone_number)
		return phone_number

	def clean_password(self):
		password = self.cleaned_data.get('password')
		validate_null(password)
		return password

	def clean(self):
		password = self.cleaned_data.get('password')
		username = self.request.user.username
		self.user_cache = authenticate(username=username, password=password)
		if self.user_cache is None:
		    raise forms.ValidationError(custom_error_messages['incorrect_password'],)
		else:
			return self.cleaned_data
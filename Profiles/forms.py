from .models import Mozart_User
from django import forms
from django_countries import countries
from Thirdauth.validations import *
from Thirdauth.forms import RegisterForm
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth

class UserInformationForm(forms.Form):

	day_of_birth = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=days,
    )

	description = forms.CharField(
		error_messages=default_error_messages,
		max_length=200,
		required=True,
	)
	facebook = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	first_name = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
	)

	google = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
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

	nationality = forms.ChoiceField(
		choices=countries,
		error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
		required=True,
	)
	
	password = forms.CharField(
	    error_messages=default_error_messages,
	    max_length=20,
	    required=True,
	    widget=forms.PasswordInput(),
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


	twitter = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	year_of_birth = forms.IntegerField(
	    error_messages=default_error_messages,
	    required=True,
	    max_value=2015,
	    min_value=1905,
	)

	youtube = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	def __init__(self, *args, **kwargs):
		super(UserInformationForm, self).__init__(*args, **kwargs)
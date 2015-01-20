from .models import Mozart_User
from django import forms
from django_countries import countries
from Thirdauth.validations import *
from Thirdauth.forms import RegisterForm
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth

class UserInformationForm(forms.Form):

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

	description = forms.CharField(
		error_messages=default_error_messages,
		max_length=200,
		required=True,
	)

	phone_number = forms.IntegerField(
		error_messages=default_error_messages,
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





   

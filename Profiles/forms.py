from .models import Mozart_User
from django import forms
from django_countries import countries
from Authentification.validations import *
from Authentification.forms import RegisterForm
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth
from django.contrib.auth import authenticate

class UserInformationForm(forms.Form):

	day_of_birth = forms.ChoiceField(
        error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
        required=True,
        choices=days,
    )

	# description = forms.CharField(
	# 	error_messages=default_error_messages,
	# 	max_length=200,
	# 	required=True,
	# )

	# facebook_url = forms.URLField(
	# 	error_messages=default_error_messages,
	# 	required=True,
	# 	max_length=30,
	# )

	# first_name = forms.CharField(
	# 	error_messages=default_error_messages,
	# 	max_length=30,
	# 	required=True,
	# )

	# google_url = forms.URLField(
	# 	error_messages=default_error_messages,
	# 	required=True,
	# 	max_length=30,
	# )

	# last_name = forms.CharField(
	# 	error_messages=default_error_messages,
	# 	max_length=30,
	# 	required=True,
	# )

	# month_of_birth = forms.ChoiceField(
	#     error_messages={
	#         'invalid_choice':('Selecciona una opcion valida'),
	#         'required': default_error_messages['required']
	#     },
	#     required=True,
	#     choices=months,
	# )

	# nationality = forms.ChoiceField(
	# 	choices=countries,
	# 	error_messages={
 #            'invalid_choice':('Selecciona una opcion valida'),
 #            'required': default_error_messages['required']
 #        },
	# 	required=True,
	# )
	
	password = forms.CharField(
	    error_messages=default_error_messages,
	    max_length=20,
	    required=True,
	    widget=forms.PasswordInput(),
	)

	# personal_homepage = forms.URLField(
	# 	error_messages=default_error_messages,
	# 	required=True,
	# 	max_length=30,
	# )

	# phone_number = forms.IntegerField(
	# 	error_messages=default_error_messages,
	# 	required=True,
	# )


	# twitter_url = forms.URLField(
	# 	error_messages=default_error_messages,
	# 	required=True,
	# 	max_length=30,
	# )

	# year_of_birth = forms.IntegerField(
	#     error_messages=default_error_messages,
	#     required=True,
	#     max_value=2015,
	#     min_value=1905,
	# )

	# youtube_url = forms.URLField(
	# 	error_messages=default_error_messages,
	# 	required=True,
	# 	max_length=30,
	# )

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.user_cache = None
		super(UserInformationForm, self).__init__(*args, **kwargs)


	def clean_day_of_birth(self):
	    day_of_birth = self.cleaned_data.get('day_of_birth')
	    validate_null(day_of_birth)
	    return day_of_birth

	# def clean_description(self):
	# 	description = self.cleaned_data.get('description')
	# 	validate_null(description)
	# 	return description

	# def clean_facebook_url(self):
	# 	facebook_url = self.cleaned_data.get('facebook_url')
	# 	validate_null(facebook_url)
	# 	return facebook_url

	# def clean_first_name(self):
	# 	first_name = self.cleaned_data.get('first_name')
	# 	validate_null(first_name)
	# 	return first_name

	# def clean_month_of_birth(self):
	#     month_of_birth = self.cleaned_data.get('month_of_birth')
	#     validate_null(month_of_birth)
	#     return month_of_birth

	# def clean_nationality(self):
	# 	nationality = self.cleaned_data.get('nationality')
	# 	validate_null(nationality)
	# 	return validate_null

	# def clean_personal_homepage(self):
	# 	personal_homepage = self.cleaned_data.get('personal_homepage')
	# 	validate_null(personal_homepage)
	# 	return personal_homepage

	# def cleaned_phone_number(self):
	# 	phone_number = self.cleaned_data.get('phone_number')
	# 	validate_null(personal_homepage)
	# 	return personal_homepage

	# def clean_twitter_url(self):
	# 	twitter_url = self.cleaned_data.get('twitter_url')
	# 	validate_null(twitter_url)
	# 	return twitter_url

	# def clean_year_of_birth(self):
	#     year_of_birth = self.cleaned_data.get('year_of_birth')
	#     validate_null(year_of_birth)
	#     return year_of_birth

	# def clean_youtube_url(self):
	# 	youtube_url = self.cleaned_data.get('youtube_url')
	# 	validate_null(youtube_url)
	# 	return youtube_url

	def clean(self):
		password = self.cleaned_data.get('password')
		username = self.request.user.username
		self.user_cache = authenticate(username=username, password=password)
		if self.user_cache is None:
		    raise forms.ValidationError(custom_error_messages['incorrect_password'],)
		else:
			return self.cleaned_data
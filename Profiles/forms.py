from .models import Mozart_User
from django import forms
from django_countries import countries
from Thirdauth.validations import *
from Thirdauth.forms import RegisterForm
from Profiles.models import days,months,type_of_users,sexuality,Mozart_User,Date_of_Birth
from django.contrib.auth import authenticate

class UserInformationForm(forms.Form):

	description = forms.CharField(
		error_messages=default_error_messages,
		max_length=200,
		required=True,
		widget=forms.Textarea()
	)

	facebook_url = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	first_name = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
	)

	google_url = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
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


	twitter_url = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	youtube_url = forms.URLField(
		error_messages=default_error_messages,
		required=True,
		max_length=30,
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.user_cache = None
		super(UserInformationForm, self).__init__(*args, **kwargs)


	def clean_description(self):
		description = self.cleaned_data.get('description')
		validate_null(description)
		return description

	def clean_facebook_url(self):
		facebook_url = self.cleaned_data.get('facebook_url')
		validate_null(facebook_url)
		return facebook_url

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		validate_null(first_name)
		return first_name

	def clean_google_url(self):
		google_url = self.cleaned_data.get('google_url')
		validate_null(google_url)
		return google_url

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		validate_null(last_name)
		return last_name

	def clean_month_of_birth(self):
	    month_of_birth = self.cleaned_data.get('month_of_birth')
	    validate_null(month_of_birth)
	    return month_of_birth

	def clean_nationality(self):
		nationality = self.cleaned_data.get('nationality')
		validate_null(nationality)
		return validate_null

	def clean_personal_homepage(self):
		personal_homepage = self.cleaned_data.get('personal_homepage')
		validate_null(personal_homepage)
		return personal_homepage

	def cleaned_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		validate_null(personal_homepage)
		return personal_homepage

	def clean_twitter_url(self):
		twitter_url = self.cleaned_data.get('twitter_url')
		validate_null(twitter_url)
		return twitter_url

	def clean_year_of_birth(self):
	    year_of_birth = self.cleaned_data.get('year_of_birth')
	    validate_null(year_of_birth)
	    return year_of_birth

	def clean_youtube_url(self):
		youtube_url = self.cleaned_data.get('youtube_url')
		validate_null(youtube_url)
		return youtube_url

	def clean(self):
		password = self.cleaned_data.get('password')
		username = self.request.user.username
		self.user_cache = authenticate(username=username, password=password)
		if self.user_cache is None:
		    raise forms.ValidationError(custom_error_messages['incorrect_password'],)
		else:
			return self.cleaned_data
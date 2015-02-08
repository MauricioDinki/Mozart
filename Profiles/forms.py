# -*- encoding: utf-8 -*-

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
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control col-xs-4','placeholder':'Username'})
	)

	first_name = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control col-xs-4','placeholder':'Nombre(s)'})
	)

	last_name = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Apellido(s)'})
	)
	
	profile_picture = forms.ImageField(
		error_messages={
			'invalid_image':('Selecciona un archivo de imagen valido'),
			'required':default_error_messages['required'],

		},
		required=False,
		widget=forms.FileInput(attrs = {'class':'form-control'}),
	)

	nationality = forms.ChoiceField(
		choices=countries,
		error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
		required=False,
		widget=forms.Select(attrs = {'class':'form-control',})
	)

	description = forms.CharField(
		error_messages=default_error_messages,
		max_length=200,
		required=False,
		widget=forms.Textarea(attrs = {'class':'form-control','placeholder':'Cuentanos Sobre ti'})
	)

	personal_homepage = forms.URLField(
		error_messages={
            'invalid':('Ingresa una url valida'),
            'required': default_error_messages['required']
        },
		required=False,
		max_length=30,
		widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Pagina Personal',})
	)

	phone_number = forms.IntegerField(
		error_messages={
			'invalid':('Ingresa un numero valido'),
			'required':default_error_messages['required']
		},
		required=False,
		widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Numero Telefonico',})
	)

	adress = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Direccion'})
	)

	city = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Ciudad'})
	)

	zip_code = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Codigo Postal'})
	)

	neighborhood = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Vecindario'})
	)

	password = forms.CharField(
	    error_messages=default_error_messages,
	    max_length=20,
	    required=False,
	    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.user_cache = None
		super(UserInformationForm, self).__init__(*args, **kwargs)

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
		return nationality

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

	def clean_adress(self):
		adress = self.cleaned_data.get('adress')
		validate_null(adress)
		return adress

	def clean_city(self):
		city = self.cleaned_data.get('city')
		validate_null(city)
		return city

	def clean_zip_code(self):
		zip_code = self.cleaned_data.get('zip_code')
		validate_null(zip_code)
		return zip_code

	def clean_neighborhood(self):
		neighborhood = self.cleaned_data.get('neighborhood')
		validate_null(neighborhood)
		return neighborhood

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

	def save(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		nationality = self.cleaned_data.get('nationality')
		description = self.cleaned_data.get('description')
		personal_homepage = self.cleaned_data.get('personal_homepage')
		phone_number = self.cleaned_data.get('phone_number')
		adress = self.cleaned_data.get('adress')
		city = self.cleaned_data.get('city')
		zip_code = self.cleaned_data.get('zip_code')
		neighborhood = self.cleaned_data.get('neighborhood')

		user_to_change =  self.request.user

		user_to_change.first_name = first_name
		user_to_change.last_name = last_name
		user_to_change.save()

		user_to_change.mozart_user.nationality = nationality
		user_to_change.mozart_user.description = description

		if self.request.FILES.get('profile_picture',False):
			user_to_change.mozart_user.profile_picture = self.request.FILES['profile_picture']

		user_to_change.mozart_user.save()
		
		user_to_change.contact.personal_homepage = personal_homepage
		user_to_change.contact.phone_number = phone_number
		user_to_change.contact.save()

		user_to_change.adress.adress = adress
		user_to_change.adress.city = city
		user_to_change.adress.zip_code = zip_code
		user_to_change.adress.neighborhood = neighborhood
		user_to_change.adress.save()

class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(
		error_messages=default_error_messages,
		required=True,
		# min_length=8,
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña Actual'}),
	)

	new_password_1 = forms.CharField(
		error_messages=default_error_messages,
		required=True,
		# min_length=8,
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Nueva Contraseña'}),
	)

	new_password_2 = forms.CharField(
		error_messages=default_error_messages,
		required=True,
		# min_length=8,
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmar Contraseña'}),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.user_cache = None
		super(ChangePasswordForm, self).__init__(*args, **kwargs)


	def clean_old_password(self):
		old_password = self.cleaned_data.get('old_password')
		validate_null(old_password)
		return old_password

	def clean_new_password_1(self):
		new_password_1 = self.cleaned_data.get('new_password_1')
		validate_null(new_password_1)
		return new_password_1

	def clean_new_password_2(self):
		new_password_1 = self.cleaned_data.get('new_password_1')
		new_password_2 = self.cleaned_data.get("new_password_2")
		validate_password(new_password_1,new_password_2)
		return new_password_1 and new_password_2

	def clean(self):
		password = self.cleaned_data.get('old_password')
		username = self.request.user.username
		self.user_cache = authenticate(username=username, password=password)
		if self.user_cache is None:
		    raise forms.ValidationError(custom_error_messages['incorrect_password'],)
		else:
			return self.cleaned_data
	
	def save(self):
		user_to_change = self.request.user
		new_password = self.cleaned_data.get('new_password_2')
		user_to_change.set_password(new_password)
		user_to_change.save()




    
# -*- encoding: utf-8 -*-

from .models import Mozart_User
from django import forms
from django.contrib.auth import authenticate
from djangular.forms import NgModelFormMixin, NgFormValidationMixin
from django_countries import countries
from Profiles.models import Mozart_User
from Thirdauth.validations import *

class UserInformationForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
	scope_prefix='information'
	form_name='informationform'

	username = forms.CharField(
		error_messages=default_error_messages,
        min_length=5,
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class':'cuadrotexto mz-field', 'placeholder':'Elije un nuevo nickname'}),
    )

	first_name = forms.CharField(
		error_messages=default_error_messages,
		min_length=2,
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs = {'class':'cuadrotexto mz-field','placeholder':'Escribe tu(s) nombre(s)'})
	)

	last_name = forms.CharField(
		error_messages=default_error_messages,
		min_length=2,
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs = {'class':'cuadrotexto mz-field', 'placeholder':'Escribe tu(s) apellido(s)'})
	)
	
	profile_picture = forms.ImageField(
		error_messages={
			'invalid_image':('Selecciona un archivo de imagen valido'),
			'required':default_error_messages['required'],
		},
		required=False,
		widget=forms.FileInput(attrs = {'accept':'image/*', 'file-upload':'', 'file-bind':'\'profilePicture\''}),
	)

	nationality = forms.ChoiceField(
		choices=countries,
		error_messages={
            'invalid_choice':('Selecciona una opcion valida'),
            'required': default_error_messages['required']
        },
		required=False,
		widget=forms.Select(attrs = {'class':'cuadrotexto mz-field',})
	)

	description = forms.CharField(
		error_messages=default_error_messages,
		max_length=200,
		required=False,
		widget=forms.Textarea(attrs = {'class':'cuadrotexto un-cuadro','placeholder':'Cuentanos Sobre ti'})
	)

	personal_homepage = forms.URLField(
		error_messages={
            'invalid':('Ingresa una url valida'),
            'required': default_error_messages['required']
        },
		required=False,
		max_length=30,
		widget=forms.URLInput(attrs={'class':'cuadrotexto mz-field', 'placeholder':'Tu página personal',})
	)

	phone_number = forms.IntegerField(
		error_messages={
			'invalid':('Ingresa un numero valido'),
			'required':default_error_messages['required']
		},
		required=False,
		widget=forms.NumberInput(attrs={'class':'cuadrotexto mz-field', 'placeholder':'Escribe tu numero telefonico',})
	)

	adress = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=False,
		widget=forms.TextInput(attrs = {'class':'cuadrotexto mz-field', 'placeholder':'Escribe tu dirección'})
	)

	city = forms.CharField(
		error_messages=default_error_messages,
		min_length=2,
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs = {'class':'cuadrotexto mz-field', 'placeholder':'Escribe el nombre de tu ciudad'})
	)

	zip_code = forms.CharField(
		error_messages=default_error_messages,
		min_length=5,
		max_length=8,
		required=False,
		widget=forms.TextInput(attrs = {'class':'cuadrotexto mz-field', 'placeholder':'Escribe tu código postal'})
	)

	neighborhood = forms.CharField(
		error_messages=default_error_messages,
		min_length=4,
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs = {'class':'cuadrotexto mz-field', 'placeholder':'Escribe el nombre de tu vecindario'})
	)

	password = forms.CharField(
	    error_messages=default_error_messages,
        min_length=6,
        max_length=40,
	    required=True,
	    widget=forms.PasswordInput(attrs={'class':'cuadrotexto mz-field', 'placeholder':'Escribe tu contraseña'}),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.user_cache = None
		self.same_username = False
		super(UserInformationForm, self).__init__(*args, **kwargs)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		lower_username = username.lower()
		validate_null(username)
		if lower_username == self.request.user.username.lower():
			self.same_username = True
			return username
		else:
			self.same_username = False
			try:
				user = User.objects.get(username = username)
			except User.DoesNotExist:
				return username
			raise forms.ValidationError(custom_error_messages['user_exist'],)

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
		username = self.cleaned_data.get('username')
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
		same_username = self.same_username

		user_to_change =  self.request.user

		if not same_username:
			user_to_change.username = username
			print "Se cambio el username"
			
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


class ChangePasswordForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
	scope_prefix='changePassword'
	form_name='passwordform'

	old_password = forms.CharField(
		error_messages=default_error_messages,
		required=True,
        min_length=6,
        max_length=40,
		widget=forms.PasswordInput(attrs={'class':'cuadrotexto mz-field','placeholder':'Escribe tu contraseña actual'}),
	)

	new_password_1 = forms.CharField(
		error_messages=default_error_messages,
		required=True,
        min_length=6,
        max_length=40,
		widget=forms.PasswordInput(attrs={'class':'cuadrotexto mz-field','placeholder':'Escribe tu nueva contraseña'}),
	)

	new_password_2 = forms.CharField(
		error_messages=default_error_messages,
		required=True,
        min_length=6,
        max_length=40,
		widget=forms.PasswordInput(attrs={'class':'cuadrotexto mz-field','placeholder':'Vuelve a escribir tu nueva contraseña', 'comparar':'changePassword.new_password_1'}),
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




    
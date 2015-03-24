# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from Works.models import Work

custom_error_messages = {
    'email_exist':'Ese email ya esta asociado una cuenta',
    'inactive': 'Su cuenta fue inhabilitada',
    'incorrect_password':'La Contraseña introducida es incorrecta',
    'invalid_login': 'Usuario o password incorrectos',
    'null_option':'Debes seleccionar una opcion',
    'password_mismatch':'Las contraseñas no coinciden',
    'user_exist':'Ese usuario ya esta ocupado',
    'work_exist':'Ese titulo ya esta ocupado',
}

default_error_messages = {
	'invalid': _('Inserte un valor valido'),
	'invalid_choice': _('Selecciona una opcion valida'),
	'invalid_image': _('Selecciona un archivo de imagen valido'),
	'max_length': _('Longitud maxima rebasada'),
	'required': _('Este campo es requerido'),
    'blank': _('El campo esta en blanco'),
    'required':  _('Este campo no puede estar vacio'),
}

def validate_blank(data):
	if str(data).isspace():
		raise forms.ValidationError(default_error_messages['blank'],)
	return data

def validate_password_matching(data_1,data_2):
	if data_1 != data_2:
		raise forms.ValidationError('Dinki')
	return data_1 and data_2

def validate_username(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			user = User.objects.get(username = data)
		except User.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['user_exist'],)

def validate_title(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			title = Work.objects.get(title = data)
		except Work.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['work_exist'],)

def validate_email(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			user = User.objects.get(email = data)
		except User.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['email_exist'],)

def validate_password(username, password):
	user_cache = authenticate(username = username, password = password)
	if user_cache is None:
		raise forms.ValidationError(custom_error_messages['incorrect_password'])
	return username and password
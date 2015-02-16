# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from Works.models import Work

custom_error_messages = {
    'blank_field': ('El campo esta en blanco'),
    'email_exist':('Ese email ya esta asociado una cuenta'),
    'inactive': ('Su cuenta fue inhabilitada'),
    'incorrect_password':('La Contraseña introducida es incorrecta'),
    'invalid_login': ('Usuario o password incorrectos'),
    'null_field' : ('Este campo es requerido'),
    'null_option':('Debes seleccionar una opcion'),
    'password_mismatch':('Las contraseñas no coinciden'),
    'user_exist':('Ese usuario ya esta ocupado'),
    'work_exist':('Ese titulo ya esta ocupado'),
}

default_error_messages = {
    'required': 'Este campo no puede estar vacio',
}

def validate_null(data):
	if str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	return data

def validate_password(data_1,data_2):
	if len(str(data_2)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data_2).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data_1 and data_2 and data_1 != data_2:
		raise forms.ValidationError(custom_error_messages['password_mismatch'],)
	return data_2

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
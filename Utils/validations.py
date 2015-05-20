# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.utils.text import slugify

default_messages = {
	'invalid': _('Inserte un valor valido'),
	'invalid_choice': _('Selecciona una opcion valida'),
	'invalid_image': _('Selecciona un archivo de imagen valido'),
	'max_length': _('Longitud maxima rebasada'),
	'required': _('Este campo es requerido'),
    'blank': _('El campo esta en blanco'),
    'unique': _('Este nombre ya no esta disponible'),
}

custom_messages = {
	'inevent': _('La fecha del evento es invalida'),
	'shevent': _('El evento no puede ser tan corto'),
}

def eval_blank(data):
	'''
		Validates for blank content
	'''
	if str(data).isspace():
		raise forms.ValidationError(default_errors['blank'],)
	return data

def eval_iexact(data, model, field):
	'''
		validates unique dinamic model fields
	'''
	original = data
	if field == 'slug':
		data = slugify(data)
	try:
		smth = model.objects.get(**{ field: data })
	except model.DoesNotExist:
		return original
	raise forms.ValidationError(default_messages['unique'],)
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

default_messages = {
	'invalid': _('Inserte un valor valido'),
	'invalid_choice': _('Selecciona una opcion valida'),
	'invalid_image': _('Selecciona un archivo de imagen valido'),
	'max_length': _('Longitud maxima rebasada'),
	'required': _('Este campo es requerido'),
    'blank': _('El campo esta en blanco'),
}

def eval_blank(data):
	if str(data).isspace():
		raise forms.ValidationError(default_errors['blank'],)
	return data
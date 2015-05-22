# -*- encoding: utf-8 -*-

from django import forms
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

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

media_error_messages = {
    'invalid_image': _('Mozart no soporta este formato de imagen'),
    'invalid_audio': _('Mozart no soporta este formato de audio'),
    'invalid_archive': _('Mozart no soporta este formato de archivo'),
}


# Data Validators


def eval_blank(data):
    if str(data).isspace():
        raise forms.ValidationError(default_errors['blank'],)
    return data


def eval_iexact(data, model, field):
    original = data
    if field == 'slug':
        data = slugify(data)
    try:
        smth = model.objects.get(**{field: data})
    except model.DoesNotExist:
        return original
    raise forms.ValidationError(default_messages['unique'],)


# Media Validators


def eval_audio(data):
    file_type = str(data.content_type)
    if file_type == 'audio/mp3':
        return data
    raise forms.ValidationError(custom_error_messages['invalid_audio'],)


def eval_image(data):
    file_type = str(data.content_type)
    if file_type == 'image/jpeg' or file_type == 'image/bmp' \
       or file_type == 'image/png':
        return data
    raise forms.ValidationError(custom_error_messages['invalid_image'],)


def eval_general(data):
    file_type = str(data.content_type)
    if file_type == 'image/jpeg' or file_type == 'image/bmp' \
       or file_type == 'image/png' or file_type == 'audio/mp3':
        return data
    raise forms.ValidationError(custom_error_messages['invalid_archive'],)

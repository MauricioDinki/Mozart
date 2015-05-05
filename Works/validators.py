# -*- encoding: utf-8 -*-
from django import forms

custom_error_messages = {
    'invalid_image':'Mozart no soporta este formato de imagen',
    'invalid_audio':'Mozart no soporta este formato de audio',
    'invalid_archive':'Mozart no soporta este formato de archivo',
}

def validate_image(data):
	file_type = str(data.content_type)
	if file_type == 'image/jpeg' or file_type == 'image/bmp' or file_type == 'image/png':
		return data
	raise forms.ValidationError(custom_error_messages['invalid_image'],)

def validate_audio(data):
	file_type = str(data.content_type)
	if file_type == 'audio/mp3':
		return data
	raise forms.ValidationError(custom_error_messages['invalid_audio'],)

def validate_general_archive(data):
	file_type = str(data.content_type)
	if file_type == 'image/jpeg' or file_type == 'image/bmp' or file_type == 'image/png' or file_type == 'audio/mp3':
		return data
	raise forms.ValidationError(custom_error_messages['invalid_archive'],)
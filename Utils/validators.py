# -*- encoding: utf-8 -*-

from django import forms
from django.utils.text import slugify
from django.contrib.auth import authenticate

from Utils.messages import default_messages, custom_messages, media_messages


# Data Validators


def eval_blank(data):
    if str(data).isspace():
        raise forms.ValidationError(default_messages['blank'],)
    return data


def eval_iexact(data, model, field):
    original = data
    lookup = '%s__iexact' % field
    if field == 'slug':
        data = slugify(data)
        lookup = field
    try:
        smth = model.objects.get(**{lookup: data})
    except model.DoesNotExist:
        return original
    raise forms.ValidationError(default_messages['unique'],)


def eval_matching(data_1, data_2):
    if data_1 != data_2:
        raise forms.ValidationError(custom_messages['mismatch'],)
    return data_1 and data_2


def eval_password(username, password):
    user_cache = authenticate(username=username, password=password)
    if user_cache is None:
        raise forms.ValidationError(custom_messages['incorrect_password'])
    return username and password


# Media Validators


def eval_audio(data):
    file_type = str(data.content_type)
    if file_type == 'audio/mp3':
        return data
    raise forms.ValidationError(media_messages['invalid_audio'],)


def eval_image(data):
    file_type = str(data.content_type)
    if file_type == 'image/jpeg' or file_type == 'image/bmp' \
       or file_type == 'image/png':
        return data
    raise forms.ValidationError(media_messages['invalid_image'],)


def eval_general(data):
    file_type = str(data.content_type)
    if file_type == 'image/jpeg' or file_type == 'image/bmp' \
       or file_type == 'image/png' or file_type == 'audio/mp3':
        return data
    raise forms.ValidationError(media_messages['invalid_archive'],)

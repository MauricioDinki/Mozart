#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.text import slugify
from django.contrib.auth import authenticate

from mozart.core.messages import custom_error_messages, media_messages


def eval_blank(data):
    if str(data).isspace():
        raise forms.ValidationError(custom_error_messages['blank'], code='blank')
    return data


def eval_iexact(data, model, field, label):
    original = data
    model_name = (model._meta.verbose_name).lower()
    field_label = (model._meta.get_field(label).verbose_name).lower()
    lookup = '%s__iexact' % field
    if field == 'slug':
        data = slugify(data)
        lookup = field
    try:
        model.objects.get(**{lookup: data})
    except model.DoesNotExist:
        return original
    raise forms.ValidationError(custom_error_messages['unique'], code='unique',
                                params={'model_name': model_name, 'field_label': field_label})


def eval_matching(data_1, data_2):
    if data_1 != data_2:
        raise forms.ValidationError(custom_error_messages['mismatch'],)


def eval_password(username, password):
    user_cache = authenticate(username=username, password=password)
    if user_cache is None:
        raise forms.ValidationError(custom_error_messages['incorrect_password'])
    return username and password


# Media Validators


def eval_audio(data):
    file_type = str(data.content_type)
    if file_type == 'audio/mp3':
        return data
    raise forms.ValidationError(media_messages['invalid_audio'],)


def eval_general(data):
    file_type = str(data.content_type)
    if file_type == 'image/jpeg' or file_type == 'image/bmp' \
       or file_type == 'image/png' or file_type == 'audio/mp3':
        return data
    raise forms.ValidationError(media_messages['invalid_archive'],)


def eval_image(data):
    file_type = str(data.content_type)
    if file_type == 'image/jpeg' or file_type == 'image/bmp' \
       or file_type == 'image/png':
        return data
    raise forms.ValidationError(media_messages['invalid_image'],)

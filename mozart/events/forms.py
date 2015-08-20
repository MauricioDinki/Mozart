#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
import time

from django import forms
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from djangular.forms import NgFormValidationMixin, NgModelForm

from mozart.core import validators
from mozart.core.messages import regex_sentences, custom_error_messages

from .models import Event


current_date = datetime.date.today()


# class EventAbstractForm(NgFormValidationMixin, NgModelForm):
class EventAbstractForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        error_messages = {
            'name': {
                'unique': _("There is a %(model_name)s with this %(field_label)s already registred") % {
                    'model_name': (model._meta.verbose_name).lower(),
                    'field_label': (model._meta.get_field('name').verbose_name).lower(),
                },
            },
        }
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'file-upload': '',
                    'file-bind': 'cover',
                    'accept': 'image/*',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                    'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ#\s]*$/',
                }
            ),
            'date': forms.TextInput(
                attrs={
                    'class': 'mozart-field active-field',
                    'type': 'date',
                    'mz-field': '',
                    'ng-change': 'validateDate()',
                    'value': current_date + datetime.timedelta(days=1),
                }
            ),
            'finish_time': forms.TextInput(
                attrs={
                    'class': 'mozart-field active-field',
                    'mz-field': '',
                    'value': '12:30',
                    'ng-change': 'validateDuration()',
                    'ng-pattern': '/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/',
                }
            ),
            'start_time': forms.TextInput(
                attrs={
                    'class': 'mozart-field active-field',
                    'mz-field': '',
                    'value': '12:00',
                    'ng-change': 'validateDuration()',
                    'ng-pattern': '/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/',
                }
            ),
            'place': forms.TextInput(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                    'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ#\s]*$/',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                    'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ\s]*$/',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(EventAbstractForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            if field == 'cover':
                self.fields[field].validators = [validators.eval_image]
            if field == 'place' or field == 'description':
                self.fields[field].validators = [validators.eval_blank]
            if field == 'name':
                self.fields[field].validators = [RegexValidator(regex=regex_sentences['numbres_and_letters_special'])]


class EventCreateForm(EventAbstractForm):
    form_controller = 'createEventCtrl'
    form_name = 'eventform'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EventCreateForm, self).__init__(*args, **kwargs)

    def eval_00(self, data):
        if data == '00':
            return '24'
        else:
            return data

    def clean_date(self):
        event_date = self.cleaned_data.get('date')
        eve = str(event_date).split('-')
        today = time.strftime("%Y-%m-%d").split('-')
        if int(eve[0]) < int(today[0]):
            raise forms.ValidationError(custom_error_messages['inevent'])
        elif int(eve[0]) == int(today[0]):
            if int(eve[1]) < int(today[1]):
                raise forms.ValidationError(custom_error_messages['inevent'])
            elif int(eve[1]) == int(today[1]):
                if int(eve[2]) < int(today[2]):
                    raise forms.ValidationError(custom_error_messages['inevent'])
        return event_date

    def clean(self):
        cleaned_data = super(EventCreateForm, self).clean()
        finish_time = cleaned_data.get('finish_time')
        start_time = cleaned_data.get('start_time')

        if start_time and finish_time:
            ini = str(start_time).split(':')
            fin = str(finish_time).split(':')

            ini[0] = self.eval_00(ini[0])
            fin[0] = self.eval_00(fin[0])

            min_fin = (int(fin[0]) * 60) + int(fin[1])
            min_ini = (int(ini[0]) * 60) + int(ini[1])

            if abs(min_fin - min_ini) < 30:
                raise forms.ValidationError(custom_error_messages['shevent'])

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return validators.eval_iexact(name, Event, 'slug', 'name')

    def save(self):
        cleaned_data = super(EventCreateForm, self).clean()

        event_instance = Event(
            user=self.request.user,
            name=cleaned_data.get('name'),
            cover=cleaned_data.get('cover'),
            date=cleaned_data.get('date'),
            description=cleaned_data.get('description'),
            finish_time=cleaned_data.get('finish_time'),
            start_time=cleaned_data.get('start_time'),
            place=cleaned_data.get('place'),
            slug=slugify(cleaned_data.get('name')),
        )

        event_instance.save()
        return event_instance

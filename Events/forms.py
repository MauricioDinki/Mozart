# -*- encoding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.utils import six 

from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from Events.models import Event
from Utils.messages import default_messages, custom_messages
from Utils.validators import eval_blank, eval_iexact, eval_image
import time, datetime

current_date = datetime.date.today()

class CreateEventForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'createEventCtrl'
    form_name = 'eventform'

    name = forms.CharField(
        label='Nombre del evento',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    place = forms.CharField(
        label='Lugar',
        min_length=4,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    start_time = forms.CharField(
        label='Hora de inicio',
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field active-field',
                'mz-field': '',
                'value':  '12:00',
                'ng-change' : 'validateDuration()',
                'ng-pattern' : '/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/',
            }
        ),
    )

    finish_time = forms.CharField(
        label='Hora de termino',
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field active-field',
                'mz-field': '',
                'value':  '12:30',
                'ng-change' : 'validateDuration()',
                'ng-pattern' : '/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/',
            }
        ),
    )

    description = forms.CharField(
        label='Descripción del evento',
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    date = forms.CharField(
        label='Fecha del evento',
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field active-field',
                'type': 'date',
                'mz-field': '',
                'ng-change' : 'validateDate()',
                'value':  current_date,
            }
        ),
    )

    cover = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'file-upload': '',
                'file-bind': 'cover',
                'accept' : 'image/*',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateEventForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].required = True
            if field == 'cover':
                self.fields[field].validators = [eval_image]
            if field == 'name' or field == 'place' or field == 'description':
                self.fields[field].validators = [RegexValidator(regex=u'^[a-zA-Z0-9_áéíóúñ#\s]*$')]

    def eval_00(self, data):
        if data == '00':
            return '24'
        else:
            return data

    def clean_date(self):
        event_date = self.cleaned_data.get('date')
        eve = str(event_date).split('-')
        tday = time.strftime("%Y-%m-%d").split('-')
        if int(eve[0]) < int(tday[0]):
            raise forms.ValidationError(custom_messages['inevent'])
        elif int(eve[0]) == int(tday[0]):
            if int(eve[1]) < int(tday[1]):
                raise forms.ValidationError(custom_messages['inevent'])
            elif int(eve[1]) == int(tday[1]):
                if int(eve[2]) < int(tday[2]):
                    raise forms.ValidationError(custom_messages['inevent'])
        return event_date

    def clean(self):
        cleaned_data = super(CreateEventForm, self).clean()
        finish_time = self.cleaned_data.get('finish_time')
        start_time = self.cleaned_data.get('start_time')

        if start_time and finish_time:
            ini = str(start_time).split(':')
            fin = str(finish_time).split(':')

            ini[0] = self.eval_00(ini[0])
            fin[0] = self.eval_00(fin[0])

            min_fin = (int(fin[0])*60) + int(fin[1])
            min_ini = (int(ini[0])*60) + int(ini[1])

            if abs(min_fin - min_ini) < 30:
                raise forms.ValidationError(custom_messages['shevent'])

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return eval_iexact(name, Event, 'slug')

    def save(self):
        cleaned_data = super(CreateEventForm, self).clean()
        print cleaned_data.get('name'),
        print cleaned_data.get('cover'),
        print cleaned_data.get('date'),
        print cleaned_data.get('description'),
        print cleaned_data.get('finish_time'),
        print cleaned_data.get('start_time'),
        print cleaned_data.get('place'),
        print slugify(cleaned_data.get('name')),

        newEvent = Event(
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

        newEvent.save()

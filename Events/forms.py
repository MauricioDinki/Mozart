# -*- encoding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.core.validators import RegexValidator
from django.utils.text import slugify
# from django.utils import six 

# from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from Events.models import Event
from Utils.messages import default_messages, custom_messages
from Utils.validators import eval_blank, eval_iexact, eval_image
import time

# class CreateEventForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
#     form_controller = 'createEventCtrl'
#     form_name = 'eventform'

#     name = forms.CharField(
#         max_length=40,
#         min_length=4,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'mozart-field empty-initial-field',
#                 'placeholder': 'Escribe un nombre para el evento.',
#                 'mz-field': '',
#             }
#         ),
#     )

#     place = forms.CharField(
#         max_length=200,
#         min_length=4,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'mozart-field empty-initial-field',
#                 'placeholder': '¿En dónde se llevará a cabo el evento?',
#                 'mz-field': '',
#             }
#         ),
#     )

#     start_time = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'mozart-field active-field',
#                 'placeholder': '¿A qué hora comienza el evento?',
#                 'mz-field': '',
#                 'value':  '12:00',
#                 'ng-change' : 'validateDuration()',
#                 'ng-pattern' : '/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/',
#             }
#         ),
#     )

#     finish_time = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'mozart-field active-field',
#                 'placeholder': '¿A qué hora finaliza el evento?',
#                 'mz-field': '',
#                 'value':  '12:30',
#                 'ng-change' : 'validateDuration()',
#                 'ng-pattern' : '/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/',
#             }
#         ),
#     )

#     description = forms.CharField(
#         max_length=1000,
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'mozart-field empty-initial-field',
#                 'mz-field': '',
#             }
#         ),
#     )

#     date = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'mozart-field active-field',
#                 'type': 'date',
#                 'mz-field': '',
#                 'ng-change' : 'validateDate()',
#                 'value':  time.strftime("%Y-%m-%d"),
#             }
#         ),
#     )

#     cover = forms.ImageField(
#         validators=[eval_image],
#         widget=forms.FileInput(
#             attrs={
#                 'file-upload': '',
#                 'file-bind': 'cover',
#                 'accept' : 'image/*',
#             }
#         ),
#     )
class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user', 'slug']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': '',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                }
            ),
            'date': forms.TextInput(
                attrs={
                    'type': 'date',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateEventForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].required = True
            if field == 'cover':
                self.fields[field].validators = [eval_image]
            if field == 'name':
                self.fields[field].validators = [RegexValidator(regex=u'^[a-zA-Z0-9]*$')]
            if field == 'place':
                self.fields[field].validators = [RegexValidator(regex=u'^[a-zA-Z0-9_áéíóúñ#\s]*$')]
            if field == 'description':
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

    def clean_finish_time(self):
        start_time = self.cleaned_data.get('start_time')
        finish_time = self.cleaned_data.get('finish_time')

        if start_time is not None:
            ini = str(start_time).split(':')
            fin = str(finish_time).split(':')

            ini[0] = self.eval_00(ini[0])
            fin[0] = self.eval_00(fin[0])

            min_fin = (int(fin[0])*60) + int(fin[1])
            min_ini = (int(ini[0])*60) + int(ini[1])

            if abs(min_fin - min_ini) < 30:
                raise forms.ValidationError(custom_messages['shevent'])

        return start_time and finish_time

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return eval_iexact(name, self.Meta.model, 'slug')

    def save(self):
        cleaned_data = super(CreateEventForm, self).clean()
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

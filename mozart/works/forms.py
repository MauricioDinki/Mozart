#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from djangular.forms import NgFormValidationMixin, NgModelForm

from mozart.core import validators
from mozart.core.messages import regex_sentences

from .models import Work


class WorkAbstractForm(NgFormValidationMixin, NgModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        error_messages = {
            'title': {
                'unique': _("There is a %(model_name)s with this %(field_label)s already registred") % {
                    'model_name': (model._meta.verbose_name).lower(),
                    'field_label': (model._meta.get_field('title').verbose_name).lower(),
                },
            },
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                    'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ\s]*$/',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                    'ng-pattern': '/^[a-zA-Z0-9_áéíóúñ\s]*$/',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                }
            ),
            'cover': forms.FileInput(
                attrs={
                    'file-upload': '',
                    'file-bind': 'cover',
                }
            ),
            'archive': forms.FileInput(
                attrs={
                    'file-upload': '',
                    'file-bind': 'cover',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(WorkAbstractForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [RegexValidator(regex=regex_sentences['numbres_and_letters_special'])]
            if field == 'cover':
                self.fields[field].validators = [validators.eval_image]
                self.fields[field].required = False
            else:
                self.fields[field].required = True
            if field == 'archive':
                self.fields[field].validators = [validators.eval_general]
            if field == 'category' or field == 'description':
                self.fields[field].validators = [validators.eval_blank]


class WorkCreateForm(WorkAbstractForm):
    form_controller = 'uploadWorkCtrl'
    form_name = 'workform'

    class Meta(WorkAbstractForm.Meta):
        fields = ['title', 'description', 'category', 'cover', 'archive']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(WorkCreateForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return validators.eval_iexact(title, Work, 'slug', 'title')

    def save(self):
        cleaned_data = super(WorkCreateForm, self).clean()
        work_instance = Work(
            user=self.request.user,
            title=cleaned_data.get('title'),
            description=cleaned_data.get('description'),
            category=cleaned_data.get('category'),
            archive=cleaned_data.get('archive'),
            slug=slugify(cleaned_data.get('title')),
        )

        if str(cleaned_data.get('archive').content_type).startswith('image'):
            work_instance.cover = work_instance.archive
            work_instance.work_type = 'image'
        elif str(cleaned_data.get('archive').content_type).startswith('audio'):
            work_instance.cover = cleaned_data.get('cover')
            work_instance.work_type = 'audio'
        else:
            work_instance.cover = cleaned_data.get('cover')
        work_instance.save()
        return work_instance


class WorkUpdateForm(WorkAbstractForm):
    form_controller = 'editWorkCtrl'
    form_name = 'editworkform'

    class Meta(WorkAbstractForm.Meta):
        fields = ['title', 'description', 'category']

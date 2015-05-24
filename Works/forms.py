# -*- encoding: utf-8 -*-

from django import forms
from django.utils import six

from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from Works.models import category, Work
from Utils.validators import eval_blank, eval_iexact, eval_image, eval_general, default_messages


class CreateWorkForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'uploadWorkCtrl'
    form_name = 'workform'

    title = forms.CharField(
        max_length=40,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'placeholder': 'Escribe un titulo para la obra',
                'mz-field': '',
            }
        ),
    )

    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    category = forms.ChoiceField(
        choices=category,
        widget=forms.Select(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    cover = forms.ImageField(
        validators=[eval_image],
        widget=forms.FileInput(
            attrs={
                'file-upload': '',
                'file-bind': 'cover',
            }
        ),
    )

    archive = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'file-upload': '',
                'file-bind': 'archive',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateWorkForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].validators = [eval_blank]
            if field == 'cover':
                self.fields[field].validators = [eval_image]
                self.fields[field].required = False
            if field == 'archive':
                self.fields[field].validators = [eval_general]
            if field != 'cover':
                self.fields[field].required = True

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return eval_iexact(title, Work, 'slug')

    def save(self):
        cleaned_data = super(CreateEventForm, self).clean()
        newWork = Work(
            user=self.request.user,
            title=cleaned_data.get('title'),
            description=cleaned_data.get('description'),
            category=cleaned_data.get('category'),
            archive=cleaned_data.get('archive'),
            slug=slugify(cleaned_data.get('title')),
        )

        if str(archive.content_type).startswith('image'):
            newWork.cover = newWork.archive
            newWork.work_type = 'image'
        elif str(archive.content_type).startswith('audio'):
            newWork.cover = cleaned_data.get('cover')
            newWork.work_type = 'audio'
        else:
            newWork.cover = cleaned_data.get('cover')
        newWork.save()


class UpdateWorkForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'editWorkCtrl'
    form_name = 'editworkform'

    class Meta:
        model = Work
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'placeholder': 'Escribe un titulo para la obra',
                    'mz-field': '',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'placeholder': 'Escribe un titulo para la obra',
                    'mz-field': '',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'placeholder': 'Escribe un titulo para la obra',
                    'mz-field': '',
                }
            ),
        }
        error_messages = {
            'title': {
                'unique': 'Ya hay una obra con ese titulo',
            },
        }

    def __init__(self, *args, **kwargs):
        super(UpdateWorkForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages.update(default_messages)
            self.fields[field].validators = [eval_blank]

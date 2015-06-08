# -*- encoding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.utils import six
from django.utils.text import slugify
from django.core.files.images import ImageFile

from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin
from sorl.thumbnail import get_thumbnail

from Utils.messages import default_messages
from Utils.validators import eval_blank, eval_iexact, eval_image, eval_general
from Works.models import category, Work


class CreateWorkForm(forms.Form):
# class CreateWorkForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'uploadWorkCtrl'
    form_name = 'workform'

    title = forms.CharField(
        max_length=40,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
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
            self.fields[field].validators = [RegexValidator(regex='^[a-zA-Z0-9\-\s]*$',), ]
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
        cleaned_data = super(CreateWorkForm, self).clean()
        newWork = Work(
            user=self.request.user,
            title=cleaned_data.get('title'),
            description=cleaned_data.get('description'),
            category=cleaned_data.get('category'),
            archive=cleaned_data.get('archive'),
            slug=slugify(cleaned_data.get('title')),
        )

        if str(cleaned_data.get('archive').content_type).startswith('image'):
            newWork.cover = newWork.archive
            newWork.work_type = 'image'
        elif str(cleaned_data.get('archive').content_type).startswith('audio'):
            newWork.cover = cleaned_data.get('cover')
            newWork.work_type = 'audio'
        else:
            newWork.cover = cleaned_data.get('cover')
        newWork.save()

        newWork.thumbnail = get_thumbnail(newWork.cover, '300x160', crop='center', quality=99).url
        newWork.save()


class UpdateWorkForm(forms.ModelForm):
    form_controller = 'editWorkCtrl'
    form_name = 'editworkform'

    class Meta:
        model = Work
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'mozart-field empty-initial-field',
                    'mz-field': '',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'mozart-field empty-initial-field',
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
            self.fields[field].validators = [RegexValidator(regex='^[a-zA-Z0-9]*$',), ]

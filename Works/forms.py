from .models import category, Work
from django import forms
from django.utils.text import slugify
from djangular.forms import NgModelFormMixin, NgFormValidationMixin
from Thirdauth.forms import default_error_messages
from Thirdauth.validations import validate_null,validate_title

class UploadWorkForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
	scope_prefix='work'
	form_name='workform'

	title = forms.CharField(
		required=True,
		min_length=4,
		max_length=40,
		widget=forms.TextInput(attrs={'class':'cuadrotexto mz-field', 'placeholder':'Escribe un titulo para la obra'}),
    )
	description = forms.CharField(
		required=True,
		min_length=1,
		max_length=1000,
		widget=forms.Textarea(attrs={'class':'cuadrotexto un-cuadro'}),
    )
	category = forms.ChoiceField(
		choices=category,
		required=True,
		widget=forms.Select(attrs={'class':'cuadrotexto mz-field'}),
	)
	archive = forms.ImageField(
		error_messages={
			'invalid_image':('Selecciona un archivo de imagen valido'),
			'required':default_error_messages['required'],
		},
		required=True,
		widget=forms.FileInput(attrs={'file-upload':'', 'file-bind':'archive'}),
	)

	cover = forms.ImageField(
		required=False,
		widget=forms.FileInput(attrs={'file-upload':'', 'file-bind':'cover', 'accept':'image/*'}),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(UploadWorkForm, self).__init__(*args, **kwargs)

	def clean_title(self):
		title = self.cleaned_data.get('title')
		validate_title(title)
		return title

	def clean_description(self):
		description = self.cleaned_data.get('description')
		validate_null(description)
		return description

	def clean_category(self):
		category = self.cleaned_data.get('category')
		validate_null('category')
		return category

	def save(self):
		title = self.cleaned_data.get('title')
		description = self.cleaned_data.get('description')
		category = self.cleaned_data.get('category')
		archive = self.cleaned_data.get('archive')
		newWork = Work(user = self.request.user,title = title, description = description, category = category , archive = archive)
		newWork.cover = newWork.archive
		newWork.slug = slugify(newWork.title)
		newWork.save()
		

from django import forms
from .models import category
from djangular.forms import NgModelFormMixin, NgFormValidationMixin

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
	archive = forms.FileField(
		required=True,
		widget=forms.FileInput(attrs={'file-upload':'', 'file-bind':'\'archive\''}),
	)
	cover = forms.ImageField(
		required=False,
		widget=forms.FileInput(attrs={'file-upload':'', 'file-bind':'\'cover\'', 'accept':'image/*'}),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(UploadWorkForm, self).__init__(*args, **kwargs)

	def clean(self):
		print self.request.FILES['archive']
		print self.request.FILES['cover']


# -*- encoding: utf-8 -*-

from .models import category, Work
from django import forms
from djangular.forms import NgModelFormMixin, NgFormValidationMixin
from Thirdauth.validations import validate_blank, validate_title, default_error_messages
from .validators import validate_image, validate_general_archive

class CreateWorkForm(forms.Form):
# class CreateWorkForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
	"""
		Form for create works
	"""
	# scope_prefix='work'
	# form_name='workform'

	title = forms.CharField(
		max_length = 40,
		# min_length = 4,
		widget = forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe un titulo para la obra',
				'mz-field':'',
			}
		),
    )

	description = forms.CharField(max_length = 1000,
		# min_length = 1,
		widget = forms.Textarea(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'mz-field':'',
			}
		),
    )

	category = forms.ChoiceField(
		choices = category,
		widget = forms.Select(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'mz-field':'',
			}
		),
	)

	cover = forms.ImageField(
		validators=[validate_image],
		widget = forms.FileInput(
			attrs = {
				'file-upload':'',
				'file-bind':'archive',
			}
		),
	)

	archive = forms.FileField()

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(CreateWorkForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].error_messages.update(default_error_messages)
			self.fields[field].validators=[validate_blank]
			if field == 'cover':
				self.fields[field].validators = [validate_image]
			if field == 'archive':
				self.fields[field].validators = [validate_general_archive]
			self.fields[field].required=False

	def clean_title(self):
		title = self.cleaned_data.get('title')
		return validate_title(title)

	def save(self):
		pass
		# title = self.cleaned_data.get('title')
		# description = self.cleaned_data.get('description')
		# category = self.cleaned_data.get('category')
		# archive = self.cleaned_data.get('archive')
		
		# newWork = Work(user = self.request.user,title = title, description = description, category = category , archive = archive)
		# newWork.cover = newWork.archive
		# newWork.save()
		# print "Se guardo la obra"
		# cover = self.cleaned_data.get('cover')
		archive = self.cleaned_data.get('archive')
		print str(archive.content_type) 
		# if str(cover.content_type) == 'image/jpeg' or str(cover.content_type) == 'image/bmp':
		# 	print "Si rifa"

class UpdateWorkForm(NgModelFormMixin, NgFormValidationMixin, forms.ModelForm):
	"""
		Form for update works
	"""
	scope_prefix='work'
	form_name='editworkform'

	class Meta:
		model = Work
		fields = ['title','description','category']
		widgets = {
        	'title':forms.TextInput(
        		attrs = {
        			'class':'mozart-field empty-initial-field',
        			'placeholder':'Escribe un titulo para la obra',
				'mz-field':'',
    			}
			),
        	'description':forms.Textarea(
        		attrs = {
        			'class':'mozart-field empty-initial-field',
				'mz-field':'',
    			}
			),
        	'category':forms.Select(
        		attrs = {
        			'class':'mozart-field empty-initial-field',
				'mz-field':'',
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
			self.fields[field].error_messages.update(default_error_messages)
			self.fields[field].validators=[validate_blank]
    

# -*- encoding: utf-8 -*-

from .models import Mozart_User
from django import forms
from django.utils import six
from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin
from django_countries import countries
from djangular.forms import NgModelFormMixin, NgFormValidationMixin
from Thirdauth.validations import *

class ChangePasswordForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
	"""
		Form for update the user password
	"""
	form_name = 'passwordform'

	old_password = forms.CharField(
		max_length=40,
		min_length=6,
		widget = forms.PasswordInput(
			attrs = {
                'class':'mozart-field empty-initial-field',
                'placeholder':'Escribe tu contraseña actual',
                'mz-field':'',
            }
		),
	)

	new_password_1 = forms.CharField(
		max_length=40,
		min_length=6,
		widget = forms.PasswordInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
                'placeholder':'Escribe tu nueva contraseña',
				'mz-field':'',
			}
		),
	)

	new_password_2 = forms.CharField(
		max_length=40,
		min_length=6,
		widget = forms.PasswordInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
                'placeholder':'Vuelve a escribir tu nueva contraseña',
				'mz-field':'',
                'mz-match':'new_password_1',
            }
		),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].error_messages.update(default_error_messages)
			self.fields[field].validators=[validate_blank]
			self.fields[field].required=True

	def clean_new_password_2(self):
		new_password_1 = self.cleaned_data.get('new_password_1')
		new_password_2 = self.cleaned_data.get('new_password_2')
		return validate_password_matching(new_password_1, new_password_2)

	def clean_old_password(self):
		password = self.cleaned_data.get('old_password')
		username = self.request.user.username
		return validate_password(username, password)

	def save(self):
		user_to_change = self.request.user
		new_password = self.cleaned_data.get('new_password_2')
		user_to_change.set_password(new_password)
		user_to_change.save()


class UserInformationForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
	"""
		Form for change user information
	"""
	form_controller = 'editInformationCtrl'
	form_name='informationform'

	username = forms.CharField(
		min_length=5,
        max_length=20,
        required = True,
        widget = forms.TextInput(
        	attrs = {
	        	'class':'mozart-field empty-initial-field', 
	        	'placeholder':'Elije un nuevo nickname',
	        	'mz-field': ''
        	}
    	),
    )

	first_name = forms.CharField(
		min_length=2,
        max_length=50,
		required = False,
		widget = forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe tu(s) nombre(s)',
				'mz-field': ''
			}
		),
	)

	last_name = forms.CharField(
		min_length=2,
        max_length=50,
		required = False,
		widget = forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe tu(s) apellido(s)',
				'mz-field': ''
			}
		),
	)
	
	profile_picture = forms.ImageField(
		required = False,
		widget = forms.FileInput(
			attrs = {
				'accept':'image/*',
				'file-upload':'',
				'file-bind':'profilePicture',
				'mz-field': ''
			}
		),
	)

	nationality = forms.ChoiceField(
		choices = countries,
		required = False,
		widget = forms.Select(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'mz-field': ''
			}
		),
	)

	description = forms.CharField(
        max_length=200,
		required = False,
		widget = forms.Textarea(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Cuentanos Sobre ti',
				'mz-field': ''
			}
		),
	)

	personal_homepage = forms.URLField(
		required = False,
		widget = forms.URLInput(
			attrs = {
				'class':'mozart-field empty-initial-field', 
				'placeholder':'Tu página personal',
				'mz-field': ''
			}
		),
	)

	phone_number = forms.IntegerField(
		required = False,
		max_value = 9999999999,
		min_value = 0,
		widget = forms.NumberInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe tu numero telefonico',
				'mz-field': '',
				'ng-pattern': ''
			}
		),
	)

	adress = forms.CharField(
		min_length=10,
		max_length=100,
		required = False,
		widget = forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe tu dirección',
				'mz-field': ''
			}
		),
	)

	city = forms.CharField(
		min_length=5,
        max_length=30,
		required = False,
		widget = forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe el nombre de tu ciudad',
				'mz-field': ''
			}
		),
	)

	zip_code = forms.CharField(
		min_length=5,
        max_length=10,
		required = False,
		widget = forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe tu código postal',
				'mz-field': ''
			}
		),
	)

	neighborhood = forms.CharField(
		min_length=4,
		max_length=200,
		required=False,
		widget=forms.TextInput(
			attrs = {
				'class':'mozart-field empty-initial-field',
				'placeholder':'Escribe el nombre de tu vecindario',
				'mz-field': ''
			}
		),
	)

	password = forms.CharField(
		min_length=6,
        max_length=40,
	    required = True,
	    widget = forms.PasswordInput(
	    	attrs = {
    			'class':'mozart-field empty-initial-field',
    			'placeholder':'Escribe tu contraseña',
    			'mz-field': ''
			}
		),
	)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.same_username = False
		super(UserInformationForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].error_messages.update(default_error_messages)
			self.fields[field].validators=[validate_blank]

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if username.lower() == self.request.user.username.lower():
			self.same_username = True
			return username
		else:
			self.same_username = False
			try:
				user = User.objects.get(username__iexact = username)
			except User.DoesNotExist:
				return username
			else:
				raise forms.ValidationError('Este username ya esta en uso', code = 'invalid_username')

	def clean_password(self):
		password = self.cleaned_data.get('password')
		username = self.request.user.username
		return validate_password(username, password)

	def save(self):
		same_username = self.same_username
		user_to_change =  self.request.user

		if not same_username:
			user_to_change.username = self.cleaned_data.get('username')
			
		user_to_change.first_name = self.cleaned_data.get('first_name')
		user_to_change.last_name = self.cleaned_data.get('last_name')
		user_to_change.save()

		user_to_change.mozart_user.nationality = self.cleaned_data.get('nationality')
		user_to_change.mozart_user.description = self.cleaned_data.get('description')

		if self.request.FILES.get('profile_picture',False):
			user_to_change.mozart_user.profile_picture = self.request.FILES['profile_picture']

		user_to_change.mozart_user.save()
		
		user_to_change.contact.personal_homepage = self.cleaned_data.get('personal_homepage')
		user_to_change.contact.phone_number = self.cleaned_data.get('phone_number')
		user_to_change.contact.save()

		user_to_change.adress.adress = self.cleaned_data.get('adress')
		user_to_change.adress.city = self.cleaned_data.get('city')
		user_to_change.adress.zip_code = self.cleaned_data.get('zip_code')
		user_to_change.adress.neighborhood = self.cleaned_data.get('neighborhood')
		user_to_change.adress.save()

# -*- encoding: utf-8 -*-

from django import forms
from .models import Event
from Thirdauth.validations import validate_blank, default_error_messages

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user','slug']
        widgets = {
        	'name': forms.TextInput(
        		attrs = {
        			'class': 'clasechida'
        		}
    		),
            'description': forms.Textarea(
            	attrs = {
            		'cols': 40, 
            		'rows': 10,
        		}
    		),
    		'date': forms.TextInput(
    			attrs = {
    				'type' : 'date',
    			}
			)
        }
    def __init__(self, *args, **kwargs):
	    super(CreateEventForm, self).__init__(*args, **kwargs)
	    for field in self.fields:
	        self.fields[field].error_messages.update(default_error_messages)
	        self.fields[field].validators=[validate_blank]
	        self.fields[field].required=True

    def val_00(self, data):
        if data == '00':
            return '24'
        else:
            return '00'

    def clean_finish_time(self):
        start_time  = self.cleaned_data.get('start_time')
    	finish_time = self.cleaned_data.get('finish_time')

        ini = str(start_time).split(':')
        fin = str(finish_time).split(':')

        ini[0] = self.val_00(ini[0])
        fin[0] = self.val_00(fin[0])

        print ini[0]
        print fin[0]


        return start_time and finish_time
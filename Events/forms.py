# -*- encoding: utf-8 -*-

import time
from Utils.validations import eval_blank
from django import forms
from .models import Event

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
            # self.fields[field].error_messages.update(default_messages)
            self.fields[field].validators=[eval_blank]
            self.fields[field].required=True

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
            raise forms.ValidationError('El evento no puede ser antes de hoy 1')
        elif int(eve[0]) == int(tday[0]):
            if int(eve[1]) < int(tday[1]):
                raise forms.ValidationError('El evento no puede ser antes de hoy 2')
            elif int(eve[1]) == int(tday[1]):
                if int(eve[2]) < int(tday[2]):
                    raise forms.ValidationError('El evento no puede ser antes de hoy 3')
        return event_date

    def clean_finish_time(self):
        start_time  = self.cleaned_data.get('start_time')
    	finish_time = self.cleaned_data.get('finish_time')

        if start_time is not None:
            ini = str(start_time).split(':')
            fin = str(finish_time).split(':')

            ini[0] = self.eval_00(ini[0])
            fin[0] = self.eval_00(fin[0])

            min_fin = (int(fin[0])*60) + int(fin[1])
            min_ini = (int(ini[0])*60) + int(ini[1])

            if abs(min_fin - min_ini) < 30:
                raise forms.ValidationError('El evento no puede ser tan corto')     
        
        return start_time and finish_time
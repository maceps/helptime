from django import forms
from django.forms import DateInput, ModelForm
from django.contrib.admin import widgets     

from .models import Event, Task

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields= '__all__'
        widgets = {
            'hide_names' :  forms.CheckboxInput(
                attrs={'class' : 'form-check_input'})
        }



class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields= ['name']
        widgets = {
            'name' :  forms.TextInput(
                attrs={'placeholder': 'New Event Name'}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= '__all__'
        widgets = {
            'task' :  forms.TextInput(
                attrs={'placeholder': 'New Task Name'}),
            'task_date' : DateInput(),
            'start_time' : TimeInput(),
            'end_time' : TimeInput(),
        }

class EventSearchForm(forms.Form):
    filter = forms.CharField(required=False, 
                             label="",
                             widget=forms.TextInput(attrs={'placeholder':'Search',
                                                           'class':'form-control'}))



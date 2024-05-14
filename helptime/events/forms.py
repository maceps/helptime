from django import forms
from django.forms import ModelForm

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

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= '__all__'
        widgets = {
            'task' :  forms.TextInput(
                attrs={'placeholder': 'New Event Name'}),
        }
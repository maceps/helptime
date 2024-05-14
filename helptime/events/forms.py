from django import forms
from django.forms import ModelForm

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields= '__all__'
        widgets = {
            'name' :  forms.TextInput(
                attrs={'placeholder': 'New Event Name'}),
        }
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime




class Event(models.Model):
    reminder_days_choice = models.TextChoices('days', '1 2 3 4 5 6 7')
    
    name = models.CharField(max_length=200, verbose_name='Event Name' )
    description = models.TextField(max_length=200, verbose_name='Event Description', blank=True)
    organization = models.CharField(max_length=100, verbose_name='Organization Name', blank=True )
    primery_contact = models.CharField(max_length=100, verbose_name='Primary Contact', blank=True)
    alternate_contact = models.CharField(max_length=100, verbose_name='Alt Contact', blank=True)
    hide_names = models.BooleanField(default=False, verbose_name='Hide Volunteer Names', blank=True)
    reminder_days = models.CharField(max_length=5, choices=reminder_days_choice, verbose_name='Days to remind in advance', default=7)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):

    task = models.CharField(max_length=200, verbose_name='Task Name' )
    description = models.CharField(max_length=200, verbose_name='Event Description', blank=True)
    task_date = models.DateField(verbose_name='Task Date', null=True, blank=True)
    start_time = models.TimeField(verbose_name='Start Time',null=True ,blank=True)
    end_time = models.TimeField(verbose_name='End Time ', null=True,blank=True )
    volunteer =models.CharField(max_length=100, verbose_name='Volunteer',  null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,  null=True, blank=True, related_name='event')

    def __str__(self):
        return self.task
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
    alternate_contact = models.CharField(max_length=100, verbose_name='Other person', blank=True)
    hide_names = models.BooleanField(default=False, verbose_name='Keep names private', blank=True)
    reminder_days = models.CharField(max_length=2, choices=reminder_days_choice, verbose_name='Days to remind in advance', default=7)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    start_date = models.DateTimeField("start date")

    def __str__(self):
        return self.name




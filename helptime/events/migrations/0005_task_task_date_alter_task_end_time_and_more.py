# Generated by Django 5.0.6 on 2024-05-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_alternate_contact_alter_event_hide_names_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_date',
            field=models.DateField(blank=True, null=True, verbose_name='Task Date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Time '),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Start Time'),
        ),
    ]

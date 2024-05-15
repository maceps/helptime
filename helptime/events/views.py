from django.http import HttpResponse, HttpResponseRedirect  # noqa: 401
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Event, Task
from .forms import EventForm, EventCreateForm, TaskForm
from django.db.models import Q


def index(request):
    # standard listing
    events = Event.objects.filter(Q(created_by=request.user) | Q(created_by__isnull=True))

    form = EventCreateForm()
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item = form.save()
            return redirect ('events:eventupdate', new_item.pk)
    return render(request, 'events/index.html', {'events' : events, 'form':form}) #to a template empty {} if no context 

@login_required  #forces a login can we add other text
def eventupdate(request, pk): 
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
   
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:index')
    return render(request, 'events/eventupdate.html', {'form':form, 'event':event})

def eventdelete(request,pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('events:index')
    return render (request, 'events/eventdelete.html', {'event': event})


def tasklist(request, pk):
    tasks = Task.objects.filter(event_id=pk)
    events = Event.objects.filter(id=pk)
    event_id = pk

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.event_id = event_id
            new_item = form.save()
            return redirect ('events:tasklist', event_id)
        
    return render(request, 'events/tasklist.html', { 'tasks': tasks , 'events' : events, 'form':form})
    

def taskupdate(request, pk): 
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    event_id = task.event_id

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.event_id = event_id
            new_item = form.save()
            return redirect ('events:tasklist', event_id)
    return render(request, 'events/taskupdate.html', {'form': form, 'task':task})

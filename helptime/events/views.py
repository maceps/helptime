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
    #todos = Todo.objects.all()  #gets data from Todo then put in the {} below
    events = Event.objects.filter(Q(created_by=request.user) | Q(created_by__isnull=True))

    # Add a new Todo .. returns to update
    form = EventCreateForm()
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item = form.save()
            #re(turn redirect('crud:index')
            return redirect ('events:update', new_item.pk)
            #return render(request, 'crud/update.html', {'form': form, 'todo':new_item.pk})
    
    return render(request, 'events/index.html', {'events' : events, 'form':form}) #to a template empty {} if no context 

@login_required  #forces a login can we add other text
def update(request, pk): 
    event = Event.objects.get(id=pk)
   # task = Task.objects.get(event_id=pk)
    form = EventForm(instance=event)
   # taskform = TaskForm(instance=task)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:index')
        #return render(request, 'events/update.html', {'form':form, 'event':event, 'taskform': taskform, 'task':task})
    return render(request, 'events/update.html', {'form':form, 'event':event})

def delete(request,pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('events:index')
    return render (request, 'events/delete.html', {'event': event})
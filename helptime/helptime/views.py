from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from events.forms import EventCreateForm, EventSearchForm


# Create your views here.
def index(request):
    #return HttpResponse("Hello world, You're at the home page.")
    context = "it worked"

    form = EventCreateForm(initial={'name':'Add Event Name Here'})
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            #new_item.created_by = request.user
            #new_item.name = 'AAA'
            new_item = form.save()
            return redirect ('events:eventupdate', new_item.pk)
        

    #return render(request, "index.html")

    return render(request, 'index.html', {'form':form})
  

def myadmin(request):
    return render(request, "myadmin.html")
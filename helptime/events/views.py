from django.http import HttpResponse, HttpResponseRedirect  # noqa: 401
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Event
from .forms import EventForm


class IndexView(generic.ListView):
    template_name = "events/index.html"
    context_object_name = "latest_event_list"

    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.order_by("-start_date")[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = "events/detail.html"
    #form_class = EventForm

    def get_context_data(self, *args, **kwargs):
            context = super(DetailView,self).get_context_data(**kwargs)
            # add extra field 
            context['all_objects'] = Event.objects.all()        
            return context

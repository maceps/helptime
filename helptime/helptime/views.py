from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
    #return HttpResponse("Hello world, You're at the home page.")
    context = "it worked"
    return render(request, "index.html")

def myadmin(request):
    return render(request, "myadmin.html")
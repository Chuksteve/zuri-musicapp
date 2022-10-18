from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Hello, Welcome to my zuri musicapp project!</h2><br>Enjoy your cool music on the go")
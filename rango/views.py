from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hi")

# Create your views here.

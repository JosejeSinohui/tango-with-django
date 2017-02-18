from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy"}
    return render(request, 'rango/index.html', context_dict)
# Create your views here.


def about(request):
    return render(request, 'rango/about.html')

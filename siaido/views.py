from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')
    

def portal(request):
    return render(request, 'home.html')
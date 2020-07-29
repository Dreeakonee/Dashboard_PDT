from django.shortcuts import render
from django.http import HttpResponse
 


# Create your views here.
def dashboard_home(request):
    return HttpResponse("<h1>dashboard home</h1>")

def dashboard_estudiante(request):
    return HttpResponse("<h1>dashboard estudiante</h1>")


from django.shortcuts import render
from django.http import HttpResponse
#from .models import TablonEjercicios
from .models import *


# Create your views here.
def dashboard_home(request):
    return HttpResponse("<h1>dashboard home</h1>")

def dashboard_estudiante(request):
    return HttpResponse("<h1>dashboard estudiante</h1>")

def info_estudiante(request):
    estudiantes = TablonEjercicios.objects.all()
    rut = 0  # Filtro por defecto

    if request.POST.get('rut'):
        rut = int(request.POST.get('rut'))
        estudiantes = estudiantes.filter(rut__in=rut)


    return render(request, "index.html", {'estudiantes': estudiantes, 'rut':rut})


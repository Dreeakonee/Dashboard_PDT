from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TablonEjercicios,Lista,Ejercicios

# Create your views here.
def index(request):
    return render(request,'cargadatos/index.html')


#class lista_tablon(TemplateView):
   # model = TablonEjercicios
  #  template_name = 'cargadatos/TablonEjercicios.html'

class lista_tablon(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'cargadatos/TablonEjercicios.html', {'tablone': TablonEjercicios.objects.all()})

 
"""class vista_lista(LoginRequiredMixin,TemplateView):
    model= Lista
    queryset= Lista.objects.filter(nrc=2020)
    template_name = 'cargadatos/vista_lista.html'"""

class vista_lista(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'cargadatos/vista_lista.html', {'vistal': Lista.objects.filter(nrc=2020)})



class vista_ejercicios_alumnos(LoginRequiredMixin,TemplateView):
    model= TablonEjercicios
    queryset= TablonEjercicios.objects.filter(rut='nico')
    template_name = 'cargadatos/vista_ejercicios_alumnos.html'

class listado_ejercicios(LoginRequiredMixin,TemplateView):
    model= Ejercicios
    template_name = 'cargadatos/listado_ejercicios.html'

class vista_grafico(TemplateView):
    template_name = 'cargadatos/grafico.html'



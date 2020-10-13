from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView #,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TablonEjercicios,Lista,Ejercicios
from django.db.models import Sum

# ALUMNO
def inicioview(request):
    return render(request,'cargadatos/inicio.html')

class estudiante_misestadistivasView(LoginRequiredMixin,TemplateView):
    template_name = "cargadatos/misestadisticas.html"


class estudiante_lista_tablonView(TemplateView):
    template_name = 'cargadatos/TablonEjercicios.html'

#PROFESOR
class profesor_lista_cursoView(LoginRequiredMixin,TemplateView):
    model= Lista
    queryset= Lista.objects.filter(nrc=2020)
    template_name = 'cargadatos/listacurso.html'

class profesor_informacion_ejerciciosView(LoginRequiredMixin,TemplateView):
    template_name = 'cargadatos/infoejercicios.html'

class profesor_estadisticas_cursosView(LoginRequiredMixin,TemplateView):
    #queryset= TablonEjercicios.objects.filter(UsuarioUnab='nico')
    template_name = 'cargadatos/estadisticascursos.html'

class profesor_estadisticasejerciciosView(TemplateView,TablonEjercicios):
    #template_name='cargadatos/graficouno.html'
    template_name='cargadatos/estadisticasejercicios.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["qs"] = TablonEjercicios.objects.all()
        context["qs"] = TablonEjercicios.objects.filter(IdEjercicio='1')
        context["qs2"] = TablonEjercicios.objects.filter(IdEjercicio='3')
        return context

"""class vistaGraficosView(LoginRequiredMixin,TemplateView):
    
    def get(self, request, **kwargs):
        try:
            return render(request, 'estadisticas.html', {'estadisticas': Estadistica.estadisticas.latest('fecha')})
        except:
            return render(request, 'estadisticas.html', {'estadisticas':
            {'confirmados_Hospital':0,
            'examenes_Hospital':0,
            'hospital_contagios':0,
            'hospital_recuperados':0
            }})"""

def grafico_datos(request):
    labels=[]
    labels2=[]
    data=[]
    data2=[]
    queryset = TablonEjercicios.objects.values('UsuarioUnab').annotate(Puntaje=Sum('Puntaje'))
    for entry in queryset:
        labels.append(entry['UsuarioUnab'])
        labels2.append(entry['UsuarioUnab'])
        data.append(entry['Puntaje'])
        data2.append(entry['Puntaje'])
    return JsonResponse(data={
        'labels': labels,
        'labels2' : labels2,
        'data': data,
        'data2': data2,
    },)
    
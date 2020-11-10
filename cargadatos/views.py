from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TablonEjercicios,Lista,Ejercicios,Estudiante,Profesor,Seccion
from django.db.models import Sum

# ALUMNO
class inicioview(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'cargadatos/inicio.html')

class estudiante_misestadistivasView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):

        #nrc_usuario=TablonEjercicios.obtener_nrc_estudiante(request.user.username)
        #only1_nrc_usuario=nrc_usuario[0:1]
        nrc_usuario=TablonEjercicios.obtener_nrc_estudiante(request.user.username)
        print(nrc_usuario)
        skills=TablonEjercicios.obtener_skills_estudiante(request.user.username)
        skillsnrc=TablonEjercicios.obtener_skills_nrc(nrc_usuario[0])
        return render(request, 'cargadatos/misestadisticas.html',{
            'skills':skills,
            'skillsnrc':skillsnrc
        })

class estudiante_estadisticasView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        usuariounab= kwargs["usuariounab"]
        nrc_usuario=TablonEjercicios.obtener_nrc_estudiante(usuariounab)
        skills=TablonEjercicios.obtener_skills_estudiante(usuariounab)
        skillsnrc=TablonEjercicios.obtener_skills_nrc(nrc_usuario[0])
        return render(request, 'cargadatos/misestadisticas.html',{
            'skills':skills,
            'skillsnrc': skillsnrc
        })




#Vista Alumno sus ejercicios desarrollados 
class estudiante_vistaejercicios(LoginRequiredMixin,ListView):
   def get(self,request,**kwargs):
        return render(request,'cargadatos/vista_ejercicios_alumnos.html',{'listaejerciciosa':TablonEjercicios.objects.filter(UsuarioUnab=request.user.username)})

class estudiante_ejercicios(LoginRequiredMixin,ListView):
   def get(self,request,**kwargs):
        ejealumno= kwargs["usuariounab"]
        return render(request,'cargadatos/vista_ejercicios_alumnos.html',{'listaejerciciosa':TablonEjercicios.objects.filter(UsuarioUnab=ejealumno)})



#PROFESOR
class profesor_lista_cursoView(LoginRequiredMixin,ListView):
    def get(self,request,**kwargs):
        nrcprofesor= kwargs["pk"]
        return render(request,'cargadatos/vista_lista.html',{'listacurso':Lista.objects.filter(nrc=nrcprofesor)})

class profesor_lista(LoginRequiredMixin, ListView):
    def get(self,request,**kwargs):
        profe= kwargs["usuario"]
        return render(request,'cargadatos/nrcprofesor.html',{'listaprofe':Seccion.objects.filter(UsuarioUnab=profe)})


class profesor_informacion_ejerciciosView(LoginRequiredMixin,ListView):
    model= Ejercicios
    template_name = 'cargadatos/listado_ejercicios.html'







class profesor_estadisticas_cursosView(LoginRequiredMixin,TemplateView):
    
    def get(self, request, **kwargs):
        nrc_curso_profe= kwargs["nrc_curso"]
        #nrc_usuario=TablonEjercicios.obtener_nrc_estudiante(usuariounab)
        #skills=TablonEjercicios.obtener_skills_estudiante(usuariounab)
        skillsnrc=TablonEjercicios.obtener_skills_nrc(nrc_curso_profe)
        skillglobal=TablonEjercicios.obtener_skills_global()
        return render(request, 'cargadatos/estadisticascursos.html',{
            'skillsnrcprofe': skillsnrc,
            'skillglobal':skillglobal
        })

    






class profesor_estadisticasejerciciosView(TemplateView,TablonEjercicios):
    #template_name='cargadatos/graficouno.html'
    template_name='cargadatos/estadisticasejercicios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["qs"] = TablonEjercicios.objects.all()
        numerito= kwargs["id_ejercicio"]

        todos_puntajes=TablonEjercicios.obtener_puntaje_por_idejercicio(numerito)

        buenas=[]
        malas=[]
        for puntaje in todos_puntajes:
            if puntaje[0] >= 1:
                buenas.append(puntaje)
            else :
                malas.append(puntaje)
        print(buenas)
        print(len(buenas))
        print(malas)
        print(len(malas))      
        print(todos_puntajes)
        print(len(todos_puntajes))
        context["context_buenas"] = len(buenas)
        context["context_malas"] = len(malas)
        context["nombre_ejercicio"]=Ejercicios.obtener_nombre_ejercicio_por_id_ejercicio(numerito)
        #print(context["nombre_ejercicio"])
        nombre_ejercicio=context["nombre_ejercicio"]
        print(nombre_ejercicio)
        return context


class nrc_profesor(LoginRequiredMixin, ListView):
    def get(self,request,**kwargs):
        return render(request,'cargadatos/nrcprofesor.html',{'listaprofe':Seccion.objects.filter(UsuarioUnab=request.user.username)})

#VistaCoordinador Todos los profesores
class profesores_todos(LoginRequiredMixin,ListView):
     model = Seccion
     queryset = Seccion.objects.all()
     template_name = 'cargadatos/Profesores.html'


#VistaCoordinador Todos los ejercicios de plataforma
class lista_tablon(LoginRequiredMixin,ListView):
    model = TablonEjercicios
    queryset = TablonEjercicios.objects.all()
    template_name = 'cargadatos/TablonEjercicios.html'

        
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
    
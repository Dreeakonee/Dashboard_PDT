from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from cargadatos.views import inicioview,estudiante_misestadistivasView,estudiante_vistaejercicios,profesor_estadisticasejerciciosView,profesor_lista_cursoView,profesor_informacion_ejerciciosView,profesor_estadisticas_cursosView,profesores_todos,lista_tablon,nrc_profesor
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url('^$',inicioview),
    url('estudiante/misestadisticas',estudiante_misestadistivasView.as_view(),name='misestadisticas'),
    url('estudiante/misejercicios', estudiante_vistaejercicios.as_view(), name='misejercicios'),
    url('profesor/estadisticasejercicios',profesor_estadisticasejerciciosView.as_view(), name='profeestadisticasejercicios'),
    url('profesor/cursos',nrc_profesor.as_view(),name='cursosprofesor'),
    url('profesor/listacurso',profesor_lista_cursoView.as_view(),name='listacurso'),
    url('profesor/informacionejercicios',profesor_informacion_ejerciciosView.as_view(),name='profeinfoejercicios'),
    url('profesor/estadisticascursos',profesor_estadisticas_cursosView.as_view(),name='profeestadisticascursos'),
    url('coordinador/profesores', profesores_todos.as_view(), name = 'coordinadorprofesores'),
    url('coordinador/ejerciciostotales',lista_tablon.as_view(), name = 'coordinadortablon'),
    url('logout/',logout_then_login, name= 'logout'),
]
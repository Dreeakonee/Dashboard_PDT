from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from cargadatos.views import inicioview,estudiante_misestadistivasView,estudiante_vistaejercicios,profesor_estadisticasejerciciosView,profesor_lista_cursoView,profesor_informacion_ejerciciosView,profesor_estadisticas_cursosView,profesores_todos,lista_tablon,nrc_profesor
from cargadatos.views import estudiante_estadisticasView,estudiante_ejercicios
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    url('^$',inicioview.as_view(),name="home"),
    url('estudiante/misestadisticas',estudiante_misestadistivasView.as_view(),name='misestadisticas'),
    url('estudiante/estadisticas/(?P<usuariounab>[\w\.]+)/',estudiante_estadisticasView.as_view(),name='estudianteestadisticas'),
    url('estudiante/misejercicios', estudiante_vistaejercicios.as_view(), name='misejercicios'),
    url('estudiante/ejercicios/(?P<usuariounab>[\w\.]+)/', estudiante_ejercicios.as_view(), name='ejercicios'),
    url('profesor/estadisticasejercicios',profesor_estadisticasejerciciosView.as_view(), name='profeestadisticasejercicios'),
    url('profesor/cursos',nrc_profesor.as_view(),name='cursosprofesor'),
    url('profesor/listacurso/(?P<pk>\d+)',profesor_lista_cursoView.as_view(),name='listacurso'),
    url('profesor/informacionejercicios',profesor_informacion_ejerciciosView.as_view(),name='profeinfoejercicios'),
    url('profesor/estadisticascursos',profesor_estadisticas_cursosView.as_view(),name='profeestadisticascursos'),
    url('coordinador/profesores',profesores_todos.as_view(), name = 'coordinadorprofesores'),
    url('coordinador/ejerciciostotales',lista_tablon.as_view(), name = 'coordinadortablon'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url('logout/',logout_then_login, name= 'logout'),
]
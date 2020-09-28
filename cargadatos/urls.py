from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from cargadatos.views import index, lista_tablon,vista_lista,vista_ejercicios_alumnos,listado_ejercicios,vista_grafico
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url('^$',index),
    url('lista/', lista_tablon.as_view(), name = "tablon_ejercicios"),
    url('Egenerales/', vista_lista.as_view(), name = "vista_lista"),
    url('alumnoestadisticas/', vista_ejercicios_alumnos.as_view()),
    url('listaejercicios/',listado_ejercicios.as_view()),
    url('grafico/',vista_grafico.as_view()),
    url('logout/',logout_then_login, name= 'logout'),

]
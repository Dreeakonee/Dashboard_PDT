from django.contrib import admin
from cargadatos.models import Profesor,Ramo,Seccion,Lista,Estudiante,Ejercicios,TablonEjercicios
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Ramo)
admin.site.register(Seccion)
admin.site.register(Lista)
admin.site.register(Estudiante)
admin.site.register(Ejercicios)
admin.site.register(TablonEjercicios)
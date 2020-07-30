from django.contrib import admin
from .models import *
"""from .models import(
    TablonEjercicios,
    Profesor,
    Estudiante,
    Seccion
)"""

from import_export import resources
from import_export.admin import ImportExportModelAdmin
import csv


# Register your models here.

class AdminResource(resources.ModelResource):
    class Meta:
        model = TablonEjercicios       

class AdminTablonEjercicios(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["rut", "nrc", "usuario", "year", "mes", "dia", "id_ejercicio", "problema", "puntaje"]
    search_fields = ["rut", "nrc", "id_ejercicio", "problema"]
    class Meta:
        model = TablonEjercicios
    resource_class = AdminResource
    
class AdminProfesor(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["nombre", "apellido", "rut", "email", "updated", "timestamp"]
    #list_display_links = ["nombre"] #Para editar campos
    list_filter = ["timestamp"]
    #list_editable = ["email"] #para editar directamente del admin
    search_fields = ["email", "nombre", "apellido", "rut"]
    class Meta:
        model = Profesor
    resource_class = AdminResource

class AdminEstudiante(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "rut", "email", "updated", "timestamp"]
    #list_display_links = ["nombre"] #Para editar campos
    list_filter = ["timestamp"]
    #list_editable = ["email"] #para editar directamente del admin
    search_fields = ["email", "nombre", "apellido", "rut"]
    class Meta:
        model = Estudiante

class AdminSeccion(admin.ModelAdmin):
    list_display = ["nrc", "semestre", "codigo_curso"]
    #list_display_links = ["nombre"] #Para editar campos
    #list_filter = ["timestamp"]
    #list_editable = ["email"] #para editar directamente del admin
    search_fields = ["nrc", "semestre", "codigo_curso"]
    class Meta:
        model = Seccion



admin.site.register(Profesor,AdminProfesor)#,AdminProfesor
admin.site.register(Estudiante, AdminEstudiante)# adminEstudiante
admin.site.register(Seccion, AdminSeccion)# adminSeccion
admin.site.register(TablonEjercicios, AdminTablonEjercicios)

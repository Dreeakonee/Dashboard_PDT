from django.contrib import admin

from .models import Profesor
from .models import Estudiante
from .models import Seccion
# Register your models here.


class AdminProfesor(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "rut", "email", "updated", "timestamp"]
    #list_display_links = ["nombre"] #Para editar campos
    list_filter = ["timestamp"]
    #list_editable = ["email"] #para editar directamente del admin
    search_fields = ["email", "nombre", "apellido", "rut"]
    class Meta:
        model = Profesor

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
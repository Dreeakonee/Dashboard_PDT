from django.contrib import admin

from .models import Profesor
# Register your models here.


class AdminProfesor(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "rut", "email", "updated", "timestamp"]
    #list_display_links = ["nombre"] #Para editar campos
    list_filter = ["timestamp"]
    #list_editable = ["email"] #para editar directamente del admin
    search_fields = ["email", "nombre", "apellido", "rut"]
    class Meta:
        model = Profesor

admin.site.register(Profesor,AdminProfesor)#,AdminProfesor
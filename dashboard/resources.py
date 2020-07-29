from import_export import resources
from .models import TablonEjercicios

class TablonEjerciciosResource(resources.ModelResource):
    class Meta:
        model = TablonEjercicios
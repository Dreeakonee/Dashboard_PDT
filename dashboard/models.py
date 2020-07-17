from django.db import models

# Create your models here.

class Profesor(models.Model):
    #id_profesor =models.
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    rut = models.IntegerField()
    email = models.EmailField(default="sinejemplo@hotmail.com")
    coordinador = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)#Para ver cuando se actualizó en la database
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)#Para ver cuando se creó en la database

    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    rut = models.IntegerField()
    email = models.EmailField(default="sinejemplo@hotmail.com")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)#Para ver cuando se actualizó en la database
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)#Para ver cuando se creó en la database
    
    def __str__(self):
        return self.nombre


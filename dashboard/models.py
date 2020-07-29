from django.db import models

# Create your models here.

class Profesor(models.Model):
    #id_profesor =models.
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    rut=models.CharField(max_length=20)
    email = models.EmailField(default="sinejemplo@hotmail.com")
    coordinador = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)#Para ver cuando se actualizó en la database
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)#Para ver cuando se creó en la database

    def __str__(self):
        return self.nombre
    


class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    rut=models.CharField(max_length=20)
    email = models.EmailField(default="sinejemplo@hotmail.com")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)#Para ver cuando se actualizó en la database
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)#Para ver cuando se creó en la database
    
    def __str__(self):
        return self.nombre



class Seccion(models.Model):
    nrc=models.CharField(max_length=20)#pk
    semestre = models.TextField()#pk
    codigo_curso = models.IntegerField()
    email = models.EmailField(default="sinejemplo@hotmail.com")

    def __str__(self):
        return self.nrc



class TablonEjercicios(models.Model):
    #correlativo=models.IntegerField()
    rut=models.CharField(max_length=20, blank=True, null=True)
    nrc=models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(default="sinejemplo@hotmail.com", blank=True, null=True)
    dia=models.CharField(max_length=20, blank=True, null=True)
    mes=models.CharField(max_length=20, blank=True, null=True)
    año=models.CharField(max_length=20, blank=True, null=True)
    idEjercicio=models.CharField(max_length=20, blank=True, null=True)
    nombreProblema=models.CharField(max_length=20, blank=True, null=True)
    puntaje=models.DecimalField(decimal_places=3, blank=True, null=True,max_digits=20)

    def __str__(self):
        return str(self.nombreProblema)



class Ejercicios(models.Model):
    IdEjercicio=models.CharField(max_length=20)
    nombreProblema=models.CharField(max_length=20)
    skill1=models.BooleanField()
    skill2=models.BooleanField()
    skill3=models.BooleanField()
    skill4=models.BooleanField()
    knowledge1=models.NullBooleanField()
    knowledge2=models.NullBooleanField()
    knowledge3=models.NullBooleanField()
    knowledge4=models.NullBooleanField()
    complejidad=models.CharField(max_length=20)
    hito=models.IntegerField()

    def __str__(self):
        return self.nombreProblema



class Ramo(models.Model):
    codigoRamo=models.CharField(max_length=20)
    nombreRamo=models.CharField(max_length=20)

    def __str__(self):
        return self.nombreRamo



class Lista(models.Model):
    #Correlativo=models.IntegerField()
    nrc=models.CharField(max_length=20)
    email = models.EmailField(default="sinejemplo@hotmail.com")
    notas=models.DecimalField(decimal_places=3, max_digits=20)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.nrc

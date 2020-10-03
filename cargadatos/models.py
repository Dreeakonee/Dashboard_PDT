from django.db import models

# Create your models here.

class Profesor(models.Model):
    UsuarioUnab=models.EmailField(primary_key=True)
    rut=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    Coordinador=models.BooleanField()
    def __str__(self):
        return self.nombre

class Ramo(models.Model):
    CodigoRamo=models.CharField(max_length=20,primary_key=True)
    NombreRamo=models.CharField(max_length=20)
    def __str__(self):
        return self.NombreRamo

class Seccion(models.Model):
    nrc=models.CharField(max_length=20,primary_key=True)
    semestre=models.CharField(max_length=20)
    CodigoRamo=models.ForeignKey(Ramo,on_delete=models.CASCADE)
    UsuarioUnab=models.ForeignKey(Profesor,on_delete=models.PROTECT)
    def __str__(self):
        return self.nrc

class Estudiante (models.Model):
    rut=models.CharField(primary_key=True,max_length=20)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    UsuarioUnab=models.EmailField(max_length=30)
    sede=models.CharField(max_length=20)
    carrera=models.CharField(max_length=50)
    jornada=models.CharField(max_length=20)
    def __str__(self):
        return str(self.UsuarioUnab)

class Lista(models.Model):
    nrc=models.ForeignKey(Seccion,on_delete=models.CASCADE)
    rut=models.ForeignKey(Estudiante,on_delete=models.PROTECT)
    notas=models.DecimalField(decimal_places=3, max_digits=20)
    estado=models.CharField(max_length=20)
    def __str__(self):
        return self.nrc

class Ejercicios(models.Model):
    IdEjercicio=models.CharField(max_length=20,primary_key=True)
    NombreProblema=models.CharField(max_length=50)
    skill1=models.BooleanField()
    skill2=models.BooleanField()
    skill3=models.BooleanField()
    skill4=models.BooleanField()
    knowledge1=models.BooleanField()
    knowledge2=models.BooleanField()
    knowledge3=models.BooleanField()
    knowledge4=models.BooleanField()
    complejidad=models.CharField(max_length=20)
    hito=models.IntegerField()
    def __str__(self):
        return self.NombreProblema

class TablonEjercicios(models.Model):
    rut=models.ForeignKey(Estudiante,null=True,on_delete=models.CASCADE)
    dia=models.CharField(max_length=20)
    mes=models.CharField(max_length=20)
    año=models.CharField(max_length=20)
    IdEjercicio=models.ForeignKey(Ejercicios,on_delete=models.PROTECT)
    Puntaje=models.DecimalField(decimal_places=3, max_digits=20)
    def __str__(self):
        return str(self.rut)


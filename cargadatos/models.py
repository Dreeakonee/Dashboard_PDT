from django.db import models
from django.db import connection

# Create your models here.

class Profesor(models.Model):
    UsuarioUnab=models.CharField(primary_key=True,max_length=20)
    #rut=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    Coordinador=models.BooleanField()
    def __str__(self):
        return self.nombre

class Ramo(models.Model):
    CodigoRamo=models.CharField(max_length=20,primary_key=True)
    NombreRamo=models.CharField(max_length=50)
    def __str__(self):
        return self.NombreRamo
    

class Seccion(models.Model):
    nrc=models.CharField(max_length=20,primary_key=True)
    semestre=models.CharField(max_length=20)
    CodigoRamo=models.ForeignKey(Ramo,on_delete=models.CASCADE)
    UsuarioUnab=models.ForeignKey(Profesor,on_delete=models.PROTECT)
    def __str__(self):
        return str(self.CodigoRamo)

class Estudiante (models.Model):
    UsuarioUnab=models.CharField(primary_key=True,max_length=20)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    #UsuarioUnab=models.EmailField(max_length=30)
    sede=models.CharField(max_length=20)
    carrera=models.CharField(max_length=50)
    jornada=models.CharField(max_length=20)
    def __str__(self):
        return self.UsuarioUnab

class Lista(models.Model):
    #IdLista=models.IntegerField(primary_key=True)
    nrc=models.ForeignKey(Seccion,on_delete=models.CASCADE)
    UsuarioUnab=models.ForeignKey(Estudiante,on_delete=models.PROTECT,null=True)#PUEDE SER FK, PERO UNA LISTA PUEDE NO TENER ALUMNOS
    notas=models.DecimalField(decimal_places=3, max_digits=20,blank=True, null=True)
    estado=models.CharField(max_length=20)
    def __str__(self):
        return str(self.nrc)

class Ejercicios(models.Model):
    IdEjercicio=models.IntegerField(primary_key=True)
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

    def obtener_nombre_ejercicio_por_id_ejercicio(id_ejercicio):
        sql='''select NombreProblema
                from cargadatos_ejercicios
                where cargadatos_ejercicios.IdEjercicio = '{0}' '''
        sql=sql.format(id_ejercicio)
        nombre_ejercicio=[]
        with connection.cursor() as cursor:
            cursor.execute(sql)
            nombre_ejercicio=cursor.fetchone()
        return nombre_ejercicio






class TablonEjercicios(models.Model):
    IdTablonEjercicios=models.IntegerField(primary_key=True)
    UsuarioUnab=models.ForeignKey(Estudiante,null=True,on_delete=models.CASCADE)
    dia=models.CharField(max_length=20)
    mes=models.CharField(max_length=20)
    año=models.CharField(max_length=20)
    IdEjercicio=models.ForeignKey(Ejercicios,on_delete=models.PROTECT)
    Puntaje=models.DecimalField(decimal_places=3, max_digits=20)
    def __str__(self):
        return str(self.UsuarioUnab)
    
    def obtener_skills_estudiante(estudiante):
        sql='''select sum(skill1),sum(skill2),sum(skill3),sum(skill4),
        sum(knowledge1),sum(knowledge2),sum(knowledge3),sum(knowledge4)
        from cargadatos_tablonejercicios, cargadatos_ejercicios
        where UsuarioUnab_id='{0}'
        and cargadatos_ejercicios.IdEjercicio=cargadatos_tablonejercicios.IdEjercicio_id'''
        sql=sql.format(estudiante)
        skills=[]
        with connection.cursor() as cursor:
            cursor.execute(sql)
            skills=cursor.fetchone()
        return skills

    def obtener_skills_nrc(nrc):
        sql='''
        select sum(skill1),sum(skill2),sum(skill3),sum(skill4),
        sum(knowledge1),sum(knowledge2),sum(knowledge3),sum(knowledge4)
        from cargadatos_tablonejercicios, cargadatos_ejercicios, cargadatos_lista
        where cargadatos_lista.nrc_id={0}
        and cargadatos_tablonejercicios.UsuarioUnab_id=cargadatos_lista.UsuarioUnab_id
        and cargadatos_ejercicios.IdEjercicio=cargadatos_tablonejercicios.IdEjercicio_id
        group by cargadatos_tablonejercicios.UsuarioUnab_id
        '''
        sql=sql.format(nrc)
        skills=[]
        with connection.cursor() as cursor:
            cursor.execute(sql)
            skills=cursor.fetchall()
        media=[0]*8
        if len(skills)>0:
            for dato in skills:
                for i in range(8):
                    media[i]=media[i]+dato[i]
            media=list(map(lambda x: x*1/len(skills),media))
        return media

    def obtener_skills_global():
        sql='''
        select nrc_id
        from cargadatos_lista
		group by nrc_id
        '''
        nrcs_curso=[]
        with connection.cursor() as cursor:
            cursor.execute(sql)
            nrcs_curso=cursor.fetchall()
        print(nrcs_curso)
        skill_global=[0]*8
        if len(nrcs_curso)>0:
            for nrc in nrcs_curso:
                skills_nrc=TablonEjercicios.obtener_skills_nrc(nrc[0])
                for i in range(8):
                    skill_global[i]=skill_global[i]+skills_nrc[i]
            skill_global=list(map(lambda x: x*1/len(nrcs_curso),skill_global))
        return skill_global

    def obtener_nrc_estudiante(nrc):
        sql= '''select nrc_id
                from cargadatos_lista
                where cargadatos_lista.UsuarioUnab_id='{0}' '''
        sql=sql.format(nrc)
        nrcs=[]
        with connection.cursor() as cursor:
            cursor.execute(sql)
            nrcs=cursor.fetchone()
        return nrcs
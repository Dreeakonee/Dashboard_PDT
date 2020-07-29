# Generated by Django 3.0.8 on 2020-07-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdEjercicio', models.CharField(max_length=20)),
                ('nombreProblema', models.CharField(max_length=20)),
                ('skill1', models.BooleanField()),
                ('skill2', models.BooleanField()),
                ('skill3', models.BooleanField()),
                ('skill4', models.BooleanField()),
                ('knowledge1', models.NullBooleanField()),
                ('knowledge2', models.NullBooleanField()),
                ('knowledge3', models.NullBooleanField()),
                ('knowledge4', models.NullBooleanField()),
                ('complejidad', models.CharField(max_length=20)),
                ('hito', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('apellido', models.CharField(max_length=120)),
                ('rut', models.CharField(max_length=20)),
                ('email', models.EmailField(default='sinejemplo@hotmail.com', max_length=254)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('nrc', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=20)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('dia', models.IntegerField(blank=True, null=True)),
                ('id_ejercicio', models.CharField(max_length=100)),
                ('problema', models.CharField(max_length=50)),
                ('puntaje', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrc', models.CharField(max_length=20)),
                ('email', models.EmailField(default='sinejemplo@hotmail.com', max_length=254)),
                ('notas', models.DecimalField(decimal_places=3, max_digits=20)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('apellido', models.CharField(max_length=120)),
                ('rut', models.CharField(max_length=20)),
                ('email', models.EmailField(default='sinejemplo@hotmail.com', max_length=254)),
                ('coordinador', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoRamo', models.CharField(max_length=20)),
                ('nombreRamo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrc', models.CharField(max_length=20)),
                ('semestre', models.TextField()),
                ('codigo_curso', models.IntegerField()),
                ('email', models.EmailField(default='sinejemplo@hotmail.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TablonEjercicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('nrc', models.CharField(max_length=20)),
                ('email', models.EmailField(default='sinejemplo@hotmail.com', max_length=254)),
                ('dia', models.CharField(max_length=20)),
                ('mes', models.CharField(max_length=20)),
                ('año', models.CharField(max_length=20)),
                ('idEjercicio', models.CharField(max_length=20)),
                ('nombreProblema', models.CharField(max_length=20)),
                ('puntaje', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
    ]

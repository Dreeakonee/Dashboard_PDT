# Generated by Django 3.0.8 on 2020-10-07 23:40

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicios',
            fields=[
                ('IdEjercicio', models.IntegerField(primary_key=True, serialize=False)),
                ('NombreProblema', models.CharField(max_length=50)),
                ('skill1', models.BooleanField()),
                ('skill2', models.BooleanField()),
                ('skill3', models.BooleanField()),
                ('skill4', models.BooleanField()),
                ('knowledge1', models.BooleanField()),
                ('knowledge2', models.BooleanField()),
                ('knowledge3', models.BooleanField()),
                ('knowledge4', models.BooleanField()),
                ('complejidad', models.CharField(max_length=20)),
                ('hito', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('UsuarioUnab', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('sede', models.CharField(max_length=20)),
                ('carrera', models.CharField(max_length=50)),
                ('jornada', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('UsuarioUnab', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('Coordinador', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('CodigoRamo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('NombreRamo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TablonEjercicios',
            fields=[
                ('IdTablonEjercicios', models.IntegerField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=20)),
                ('mes', models.CharField(max_length=20)),
                ('año', models.CharField(max_length=20)),
                ('Puntaje', models.DecimalField(decimal_places=3, max_digits=20)),
                ('IdEjercicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cargadatos.Ejercicios')),
                ('UsuarioUnab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cargadatos.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='profesor_estadisticasejerciciosView',
            fields=[
                ('tablonejercicios_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cargadatos.TablonEjercicios')),
            ],
            bases=(django.views.generic.base.TemplateView, 'cargadatos.tablonejercicios'),
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('nrc', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('semestre', models.CharField(max_length=20)),
                ('CodigoRamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargadatos.Ramo')),
                ('UsuarioUnab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cargadatos.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('estado', models.CharField(max_length=20)),
                ('UsuarioUnab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cargadatos.Estudiante')),
                ('nrc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargadatos.Seccion')),
            ],
        ),
    ]

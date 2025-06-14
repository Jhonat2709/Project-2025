from django.db import models

# Modelos de toda la aplicacion.


# Periodos académicos
class Periodos(models.Model):
    nombre = models.CharField(max_length=6)


# Carreras (categorías)
class Carreras(models.Model):
    nombre = models.CharField(max_length=25)


# Palabras clave de la tesis
class PalabrasClave(models.Model):
    palabra = models.CharField(max_length=20)


# Autores de las tesis
class Autores(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)


# Tesis
class Tesis(models.Model):
    resumen = models.CharField(max_length=1000)
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)
    numero_paginas = models.IntegerField()
    periodo_academico = models.ForeignKey(
        Periodos,
        on_delete=models.CASCADE,
    )
    carrera = models.ForeignKey(
        Carreras,
        on_delete=models.CASCADE,
    )
    documento = models.FileField(upload_to='thesis/')
    estado = models.BooleanField(default=True)


# Tabla puente entre Tesis y Autores
class TesisAutores(models.Model):
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE)
    autor = models.ForeignKey(
        Autores,
        on_delete=models.CASCADE,
    )


# Tabla puente entre tesis y palabras clave
class TesisPalabrasClave(models.Model):
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE)
    palabras_clave = models.ForeignKey(PalabrasClave, on_delete=models.CASCADE)


# PERF: Issue completado

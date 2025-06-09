from django.db import models

"""
Estas clases (Curso, Estudiante, Profesor, Entregable) en el archivo models.py de Django definen modelos de datos. Es decir, representan tablas en la base de datos, y cada clase es una tabla con sus campos (columnas).

🧩 ¿Para qué se agregan estas clases?
Para que Django pueda:

Crear automáticamente la base de datos con esas estructuras (tablas).

Guardar, consultar, actualizar y eliminar datos relacionados a cursos, estudiantes, profesores, entregables, etc.

Facilitarte una interfaz administrativa para gestionar estos registros.
"""

class Curso(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    camada = models.IntegerField()  # Campo entero

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 100 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 100 caracteres
    email = models.EmailField()  # Campo de email

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 30 caracteres
    email = models.EmailField()  # Campo de email
    profesion = models.CharField(max_length=50)  # Campo string de 50 caracteres

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    fechaDeEntrega = models.DateField()  # Campo de fecha
    entregado = models.BooleanField()  # Campo booleano

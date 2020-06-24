from django.db import models

class Autor(models.Model):
    nombre= models.CharField(max_length=50)
    matricula= models.CharField(max_length=50)

class Libros(models.Model):
    titulo= models.CharField(max_length=50)
    codigo= models.IntegerField(null=True)
    editorial= models.CharField(max_length=50, null=True)
    CantPags= models.IntegerField(null=True)
    CantCopias= models.CharField(max_length=50, null=True)

class usuarios(models.Model):
    codigo= models.IntegerField
    nombre= models.CharField
    direccion= models.CharField
    telefono= models.IntegerField


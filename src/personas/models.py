from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=30,blank=False) #ahora un campo es obligatorio
    apellidos = models.CharField(max_length=30,blank=False)
    edad = models.IntegerField(blank=False)
    donador = models.BooleanField()
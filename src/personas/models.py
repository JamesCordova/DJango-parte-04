from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.TextField(max_length=30,blank=False) #ahora un campo es obligatorio
    apellidos = models.TextField(max_length=30,blank=False)
    edad = models.TextField()
    donador = models.BooleanField()
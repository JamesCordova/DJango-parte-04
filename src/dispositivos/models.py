from django.db import models

# Create your models here.
class Dispositivo(models.Model):
    nombre = models.TextField()
    marca = models.TextField()
    numero = models.IntegerField()
    
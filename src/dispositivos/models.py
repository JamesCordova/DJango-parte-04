from django.db import models

# Create your models here.
class Dispositivo(models.Model):
    nombre = models.TextField(max_length=10,blank=False)
    marca = models.CharField(default="unknown",max_length=10)
    numero = models.IntegerField(blank=False)
    funcional = models.BooleanField()
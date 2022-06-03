from django.db import models

# Create your models here.
class Lugar(model.Model):
    nombre = models.TextField(max_length=30,blank=True)
    nroTuristasYear = models.IntegerField()
    pais = models.CharField(max_length=20,primary_key=True)
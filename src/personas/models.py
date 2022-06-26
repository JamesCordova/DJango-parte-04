from django.db import models
from django.urls import reverse

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=30,blank=False) #ahora un campo es obligatorio
    apellidos = models.CharField(max_length=30,blank=False)
    edad = models.IntegerField(blank=False)
    donador = models.BooleanField(default=False)

    def get_absolute_url(self):
        #return '/personas/' + str(self.id) + '/' # no es dinamico asi que para hacerlo de esa manera usaremos reverse
        return reverse('browsing', kwargs = {'myID': self.id})
    
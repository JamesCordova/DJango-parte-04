from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = {
            'nombres',
            'apellidos',
            'edad',
            #'donador',
        }

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(label = 'Tu nombre')
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 18)
    donador = forms.BooleanField()
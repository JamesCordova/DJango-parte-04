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
    #nombres = forms.CharField(label = 'Tu nombre')
    nombres = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Coloca solo tu nombre, por favor',
                'id': 'nombreid',
                'class': 'special',
                'cols': '10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 18)
    donador = forms.BooleanField()
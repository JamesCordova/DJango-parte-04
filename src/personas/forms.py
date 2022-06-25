from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = {
            'nombres',
            'apellidos',
            'edad',
            'donador',
        }
    
    def clean_nombres(self, *args, **kwargs):
        print('usando clean_nombres')
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra debe ser mayúscula')

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
    edad = forms.IntegerField(initial = 18) # frente a problemas con algunos tags que no soporten el tipo de campo
    donador = forms.BooleanField() # al parecer no arruinan nada, ya que se hace la misma validacion,
    #si se necesita de un numero, pediran un numero, si es boolean, un string con caracteres sera True
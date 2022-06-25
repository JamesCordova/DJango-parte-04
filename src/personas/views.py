from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 2)
    oldContext = {
        'nombre': obj.nombres,
        'edad': obj.edad,
    }
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    ''' version antigua del form
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form': form
    }'''
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

def personaCreateViewOld(request):
    obj = Persona.objects.get(id = 11)
    form = PersonaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form': form
    }
    return render(request, 'personas/personasCreate old.html', context)

def personaAnotherCreateView(request):
    #form = RawPersonaForm(request.POST) # dejando esto a un lado
    form = RawPersonaForm() # request.get si lo fuera tendriamos problemas con el comentario anterior como linea de codigo
    if request.method =='POST':
        form = RawPersonaForm(request.POST) # ahora comprobamos si es POST para luego recien enviar los datos en POST al form
        if form.is_valid():
            print(form.cleaned_data)
            # ahora grabamos los datos
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate old.html', context)
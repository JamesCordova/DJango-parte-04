from datetime import datetime
from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args,**kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 333,
        'myList': [33, 44, 55]
    }
    return render(request,'home.html',myContext)

def myOtraVista(request, *args, **kwargs):
    return HttpResponse('<h1>Solo otra pagina</h1>')

def pagina404(request, *args, **kwargs):
    context = {
        'presentacion': "I'm a student and I choose 'everything'",
        'descripcion': 'Hay demasiadas cosas por demostrar\ncomo varios textos de planos a Html\nasi como agregar mas contenido',
        'list1': ['a', 'e', 'i'],
        'list2': ['o', 'u'],
        'curso': 'programacion',
        'fecha': datetime.now(),
        'valor': '',
        'boolean1': True,
        'boolean2': False,
        'otroValor': None,
        'dict':[{'nombre': 'Luis','edad':32}, {'nombre': 'Jhon','edad':53}],
    }
    return render(request,'404.html', context)

def paginaNoAccess(request, *args, **kwargs):
    myContext = {
        'text': 'Un ejemplo de texto',
        'number': 44.3,
        'list': [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97],
        'listVoid': [],
        'listFilled': ['natación', 'futbol', 'voley', 'basquet'], # deportes que me agradan
    }
    return render(request,'noAccess.html', myContext)

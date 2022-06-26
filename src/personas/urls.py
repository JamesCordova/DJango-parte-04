from django.urls import path

# Persona
from personas.views import (
    personaTestView, 
    personaCreateView, 
    searchForHelp, 
    personaCreateViewOld, 
    personaAnotherCreateView,
    personaShowObject,
    personasDeleteView,
    personasListView,
)

# establecer el nombre de la app, que seria localhost:8000/<NOMBRE:app_name>/<las rutas en este archivo>/
app_name = 'personas'
urlpatterns = [
    path('ejemplo/', personaTestView, name='Otro'),
    path('agregar/', personaCreateView, name='createPersona'),
    path('search', searchForHelp, name='buscar'),
    path('addPersona/', personaCreateViewOld, name='Crear una persona más'),
    path('anotherAdd/', personaAnotherCreateView, name='Otro agregar persona'),
    path('<int:myID>/', personaShowObject, name='browsing'),
    path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    path('', personasListView, name='listing'),
]
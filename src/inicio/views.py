from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,'home.html',{})

def myOtraVista(request, *args, **kwargs):
    return HttpResponse('<h1>Solo otra pagina</h1>')
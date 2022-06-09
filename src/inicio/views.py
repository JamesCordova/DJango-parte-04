from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,'home.html',{})

def myOtraVista(request, *args, **kwargs):
    return HttpResponse('<h1>Solo otra pagina</h1>')

def pagina404(request, *args, **kwargs):
    return render(request,'404.html',{})

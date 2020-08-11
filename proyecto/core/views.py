from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contacto(request):
    return render(request, 'core/contact.html')

def donaciones(request):
    return render(request, 'core/donaciones.html')
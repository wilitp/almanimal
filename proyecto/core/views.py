from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contacto(request):

    if request.method == 'POST':

        nombre = request.POST.get('first_name')

        if nombre == "":
            return HttpResponse("Completá los campos obligatorios")
        
        print(nombre)
        return render(request, 'core/contact.html')

    return render(request, 'core/contact.html')

def donaciones(request):
    return render(request, 'core/donaciones.html')
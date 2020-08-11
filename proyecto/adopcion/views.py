from django.shortcuts import render


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Animal

# Create your views here.


def adopcion(request):
    return render(request, 'adopcion/adopcion.html')



class AdopcionListView(ListView ):
    
    model = Animal
    template_name = 'adopcion/adopcion_list.html'


class AdopcionDetailView(DetailView):

    model = Animal
    template_name = 'adopcion/adopcion_detail.html'
    



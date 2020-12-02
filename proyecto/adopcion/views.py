from django.shortcuts import render, redirect


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Animal
from core.models import PaginaAdopcion

from .forms import AnimalForm

from django.contrib.auth.models import User

# Create your views here.



class AdopcionListView(ListView):
    
    model = Animal
    template_name = 'adopcion/adopcion_list.html'
    queryset = Animal.objects.all().order_by('-id').filter(publicado=True)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        queries = super(AdopcionListView, self).get_context_data(**kwargs)
        queries['seo_description'] = PaginaAdopcion.objects.get(id=1).seo_description
        return queries

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(tipo_animal=query, publicado=True).order_by('-id')
        elif query == None or query == "":
            object_list = self.model.objects.all().order_by('-id').filter(publicado=True)
        else:
            object_list = self.model.objects.none()
        return object_list 


class AdopcionDetailView(DetailView):

    model = Animal
    template_name = 'adopcion/adopcion_detail.html'

class AdopcionFormView(CreateView):

    template_name = 'adopcion/adopcion_form.html'
    form_class = AnimalForm

    def post(self, request):
        
        if request.method == 'POST':

            form = AnimalForm(request.POST, request.FILES)

            if form.is_valid():

                a = form.save(commit=False)
                a.dueño = User.objects.get(id=request.user.id)
                a.save()

                return redirect('adopcion')


class AdopcionUpdateView(UpdateView):

    model = Animal
    form_class = AnimalForm
    template_name = 'adopcion/adopcion_edit.html'
    success_url = '/adopcion/'


class AdopcionDeleteView(DeleteView):

    model = Animal
    success_url = '/adopcion/'
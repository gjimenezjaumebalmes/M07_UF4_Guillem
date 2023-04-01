import json
from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Profesor


def homePageView(request):
    return render(request, 'principal.html')


def profesorado(request):
    with open('data/datos.json') as f:
        data = json.load(f)
    profesorado = data['profesorado']
    return render(request, 'profesorado.html', {'profesorado': profesorado})

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'profesor_detail.html'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        # Comprobar si el archivo JSON existe
        try:
            with open('data/datos.json', 'r') as f:
                profesores_data = json.load(f)
        except FileNotFoundError:
            raise Http404('Archivo no encontrado')

        # Obtener el profesor con el id correspondiente
        profesor_id = self.kwargs.get('pk')

        if profesor_id is None:
            raise Http404('Profesor no encontrado')

        try:
            profesor_data = next((p for p in profesores_data['profesorado'] if p['id'] == int(profesor_id)), None)
        except ValueError:
            raise Http404('Profesor no encontrado')

        # Comprobar si se ha encontrado el profesor
        if not profesor_data:
            raise Http404('Profesor no encontrado')

        # Crear una instancia del modelo Profesor con los datos del profesor encontrado
        profesor = Profesor(**profesor_data)

        return profesor


def alumnado(request):
    with open('data/datos.json') as f:
        data = json.load(f)
    alumnado = data['alumnado']
    return render(request, 'alumnado.html', {'alumnado': alumnado})

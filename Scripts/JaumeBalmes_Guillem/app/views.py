from django.shortcuts import render
import json
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
    context_object_name = 'profesor'

def alumnado(request):
    with open('data/datos.json') as f:
        data = json.load(f)
    alumnado = data['alumnado']
    return render(request, 'alumnado.html', {'alumnado': alumnado})
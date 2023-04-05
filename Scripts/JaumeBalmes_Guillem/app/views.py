from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Profesor, Alumno
from django.http import Http404

def homePageView(request):
    return render(request, 'principal.html')

def profesorado(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesorado.html', {'profesores': profesores})

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'profesor_detail.html'
    pk_url_kwarg = 'pk'

def alumnado(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnado.html', {'alumnos': alumnos})

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'alumno_detail.html'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        alumno_id = self.kwargs.get('pk')
        try:
            alumno = Alumno.objects.get(pk=alumno_id)
        except Alumno.DoesNotExist:
            raise Http404('Alumno no encontrado')
        return alumno

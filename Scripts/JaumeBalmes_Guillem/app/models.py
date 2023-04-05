from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.db import models

class Profesor(models.Model):
    id  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

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

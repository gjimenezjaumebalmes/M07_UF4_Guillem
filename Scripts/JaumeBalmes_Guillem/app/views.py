from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import Http404

from .models import Profesor, Alumno
from .forms import ProfesorForm, AlumnoForm


def homePageView(request):
    return render(request, 'principal.html')


def profesorado(request):
    profesores = Profesor.objects.all()

    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()

    return render(request, 'profesorado.html', {'profesores': profesores, 'form': form})


class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'profesor_detail.html'
    pk_url_kwarg = 'pk'


def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesor_list')
    return render(request, 'profesor_delete.html', {'profesor': profesor})


def alumnado(request):
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()

    return render(request, 'alumnado.html', {'alumnos': alumnos, 'form': form})


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


def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_list')
    return render(request, 'alumno_delete.html', {'alumno': alumno})


class ProfesorDeleteView(DetailView):
    model = Profesor
    template_name = 'profesor_delete.html'
    success_url = reverse_lazy('profesor_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class AlumnoDeleteView(DetailView):
    model = Alumno
    template_name = 'alumno_delete.html'
    success_url = reverse_lazy('alumno_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

def profesor_edit(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)

    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.save()
            return redirect('profesor_detail', pk=profesor.pk)
    else:
        form = ProfesorForm(instance=profesor)

    return render(request, 'profesor_edit.html', {'form': form})


def alumno_edit(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            return redirect('alumno_detail', pk=alumno.pk)
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumno_edit.html', {'form': form})
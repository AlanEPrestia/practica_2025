from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

# def lista_estudiantes(request):
#     estudiantes = Estudiante.objects.all()
#     return render(request, 'estudiantes_list.html', {'estudiantes': estudiantes})

# def detalle_estudiante(request, pk):
#     estudiante = get_object_or_404(Estudiante, pk=pk)
#     return render(request, 'estudiante_detail.html', {'estudiante': estudiante})


def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Estudiante, Profesor, Curso, Entregable
from ..forms import CursoFormulario, ProfesorFormulario

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

def cursoFormulario(request):
      return render(request, "AppCoder/formulario/cursoFormulario.html")

def cursoFormulario2(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/cursos.html")
      else:
            miFormulario = CursoFormulario() # Formulario vacio para construir el html
 
      return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})

def profesorFormulario(request):

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # aquí llega toda la información del html
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return render(request, "AppCoder/index.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el html

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})

"""
[Usuario entra por primera vez]
→ request.method == GET
→ muestra el formulario vacío

[Usuario llena el formulario y lo envía]
→ request.method == POST
→ se valida el formulario
→ si es válido:
   → se crea y guarda el profesor
   → se muestra la lista de profesores actualizada
→ si NO es válido:
   → se vuelve a mostrar el formulario con errores
"""

def busquedaCamada(request):
    return render(request, "AppCoder/formulario/busquedaCamada.html")


def buscar(request):
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        camada = request.GET['camada']
        # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
        # sin importar si las letras están en mayúsculas o minúsculas
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/formulario/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:
        respuesta = "No enviaste datos"

        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)

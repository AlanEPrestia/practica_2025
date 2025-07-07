from django.shortcuts import render #se utiliza para importar la función render, que es una herramienta fundamental en Django para devolver una respuesta HTTP con contenido HTML, normalmente al cargar una plantilla (template).
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Profesor

def leerProfesores(request):
      profesores = Profesor.objects.all() #trae todos los profesores
      return render(request, "AppCoder/formulario/leerProfesores.html", {"profesores": profesores})

def profesorFormulario(request):  
    # Vista para crear un nuevo profesor a través de un formulario

    if request.method == 'POST':  
        # Si el usuario envió el formulario (método POST), procesamos los datos

        miFormulario = ProfesorFormulario(request.POST)  
        # Creamos una instancia del formulario con los datos enviados desde el HTML

        if miFormulario.is_valid():  
            # Verificamos que los datos sean válidos (cumplen las reglas del formulario)

            informacion = miFormulario.cleaned_data  
            # Accedemos a los datos limpios y validados del formulario (devuelve un diccionario)

            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            # Creamos una instancia del modelo Profesor con los datos ingresados

            profesor.save()  
            # Guardamos el nuevo profesor en la base de datos

            return leerProfesores(request)
            # Redirigimos a la vista que muestra la lista de profesores

    else:
        miFormulario = ProfesorFormulario()  
        # Si es una solicitud GET (primera vez que se accede), mostramos el formulario vacío

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})  
    # Renderizamos el formulario en el template HTML, pasando el formulario como contexto


def eliminarProfesor(request, id_profesor):
 
    profesor = Profesor.objects.get(id=id_profesor)  # Obtengo el profesor por su ID
    profesor.delete()
 
    return leerProfesores(request)
    # vuelvo al menú
    # profesores = Profesor.objects.all()  # trae todos los profesores
    # return render(request, "AppCoder/formulario/leerProfesores.html", {"profesores": profesores})

"""
def eliminarProfesor(request, id_profesor):
    # Vista para eliminar un profesor según su ID recibido desde la URL

    profesor = Profesor.objects.get(id=id_profesor)
    # Obtenemos el objeto Profesor correspondiente al ID recibido

    profesor.delete()
    # Eliminamos ese profesor de la base de datos

    return leerProfesores(request)
    # Mostramos la lista actualizada de profesores
    # (Se recomienda usar redirect('profesores') para una redirección real)
"""


def editarProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)  # Recibe el nombre del profesor que vamos a modificar
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            return leerProfesores(request)

    else:
        miFormulario = ProfesorFormulario(
            initial={
                'nombre': profesor.nombre,
                'apellido': profesor.apellido,
                'email': profesor.email,
                'profesion': profesor.profesion
                }
        )

    return render(request, "AppCoder/formulario/editarProfesor.html", {"miFormulario": miFormulario, "profesor_id": profesor.id})

"""
def editarProfesor(request, id_profesor):
    # Vista para editar los datos de un profesor según su ID

    profesor = Profesor.objects.get(id=id_profesor)
    # Buscamos el profesor a editar en la base de datos

    if request.method == 'POST':
        # Si el formulario fue enviado (método POST), procesamos los datos

        miFormulario = ProfesorFormulario(request.POST)
        # Creamos el formulario con los datos enviados por el usuario

        if miFormulario.is_valid():
            # Si los datos del formulario son válidos, los procesamos

            informacion = miFormulario.cleaned_data
            # Obtenemos los datos validados como diccionario

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            # Asignamos los nuevos valores al objeto profesor

            profesor.save()
            # Guardamos los cambios en la base de datos

            return leerProfesores(request)
            # Mostramos la lista actualizada de profesores
            # (Se recomienda usar redirect('profesores') para una redirección real)

    else:
        # Si la solicitud es GET, mostramos el formulario con los datos actuales

        miFormulario = ProfesorFormulario(
            initial={
                'nombre': profesor.nombre,
                'apellido': profesor.apellido,
                'email': profesor.email,
                'profesion': profesor.profesion
            }
        )
        # Creamos el formulario prellenado con los datos del profesor

    return render(request, "AppCoder/formulario/editarProfesor.html", {"miFormulario": miFormulario, "profesor_id": profesor.id})
    # Renderizamos el formulario en la plantilla para que el usuario pueda editar
"""
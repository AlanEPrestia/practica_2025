from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

### CUARTO
def index(request):
	return render(request, 'core/index.html') # ULTIMO ESTO

#### PRIMERO
def saludar(request):
    return HttpResponse("Hola desde Django")

### SEGUNDO
def saludar_con_etiqueta(request):
	return HttpResponse('<h1 style="color:red"> Hola </h1>') # 2° ESTO

### TERCERO
def saludar_con_parametros(request, nombre: str, apellido: str): # 3° ESTO
	nombre = nombre.capitalize()
	apellido = apellido.upper()
	return HttpResponse(f'{apellido}, {nombre}')

### QUINTO

def probando_template(request):
    contexto = {
        "nombre": "Nicolas",
        "apellido": "Catalano",
        "dia": datetime.now().date(),
        "notas": [10, 2, 4, 7, 3], #### SE MUESTRA EN EL SEGUNDO EJEMPLO
        "notas_malas": [6, 4, 2], #### SE MUESTRA EN EL SEGUNDO EJEMPLO 
    }
    return render(request, "core/template1.html", contexto)
"""
🔍 ¿Qué hace render()?
La función render() de Django hace tres cosas a la vez:
Carga la plantilla HTML que le pasás.
Rellena la plantilla con los datos del contexto (el diccionario con tus variables).
Devuelve un objeto HttpResponse con el HTML generado como contenido.
"""
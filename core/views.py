from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'core/index.html') 


def saludar(request):
    return HttpResponse("Hola desde Django")


def saludar_con_etiqueta(request):
	return HttpResponse('<h1 style="color:red"> Hola </h1>') 


def saludar_con_parametros(request, nombre: str, apellido: str): 
	nombre = nombre.capitalize()
	apellido = apellido.upper()
	return HttpResponse(f'{apellido}, {nombre}')



def probando_template(request):
    contexto = {
        "nombre": "Alan",
        "apellido": "Prestia",
        "dia": datetime.now().date(),
        "notas": [10, 2, 4, 7, 3], 
        "notas_malas": [6, 4, 2], 
    }
    return render(request, "core/template1.html", contexto)
"""
🔍 ¿Qué hace render()?
La función render() de Django hace tres cosas a la vez:
Carga la plantilla HTML que le pasás.
Rellena la plantilla con los datos del contexto (el diccionario con tus variables).
Devuelve un objeto HttpResponse con el HTML generado como contenido.
"""
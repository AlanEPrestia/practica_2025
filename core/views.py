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
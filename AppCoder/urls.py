from django.urls import path
from .views import cursos, profesores, estudiantes, entregables, inicio, cursoFormulario, cursoFormulario2,profesorFormulario,busquedaCamada, buscar

urlpatterns = [
    # path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    # path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),

    path('cursoFormulario',cursoFormulario, name='cursoFormulario'),
    path('cursoFormulario2',cursoFormulario2, name='cursoFormulario2'),
    path('profesorFormulario', profesorFormulario, name="profesorFormulario"),

    path('busquedaCamada/', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name='buscar'),

]
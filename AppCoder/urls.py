from django.urls import path
from django.contrib.auth.views import LogoutView

from AppCoder.views.other import  profesores, estudiantes, entregables, inicio, cursoFormulario, cursoFormulario2,profesorFormulario,busquedaCamada, buscar
from AppCoder.views.profesores import leerProfesores,eliminarProfesor,editarProfesor,profesorFormulario
from AppCoder.views.cursos import CursoListView, CursoDetailView, CursoCreateView, CursoUpdateView, CursoDeleteView
from AppCoder.views.usuario import login_request,register,editarPerfil,upload_avatar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),

    path('cursoFormulario',cursoFormulario, name='cursoFormulario'),
    path('cursoFormulario2',cursoFormulario2, name='cursoFormulario2'),
    path('profesorFormulario', profesorFormulario, name="profesorFormulario"),

    path('busquedaCamada/', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name='buscar'),

    path('profesores/',leerProfesores,name='profesores'),
    path('profesorFormulario/', profesorFormulario, name="profesorFormulario"),
    path('eliminarProfesor/<int:id_profesor>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<int:id_profesor>', editarProfesor, name="editarProfesor"),


    path('cursos/', CursoListView.as_view(), name='cursos'), 
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='cursos_detail'),
    path('cursos/nuevo/', CursoCreateView.as_view(), name='cursos_new'),
    path('cursos/editar/<int:pk>/', CursoUpdateView.as_view(), name='cursos_edit'),
    path('cursos/borrar/<int:pk>/', CursoDeleteView.as_view(), name='cursos_delete'),

    path('login', login_request, name="login"),
    path('registro', register, name='registro'),
    path('logout', LogoutView.as_view(template_name='AppCoder/usuario/logout.html'), name='logout'),

    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),

]


"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), ### CUARTO (en primer lugar estaba como path('index/', views.index))
    path('saludar', views.saludar), ### PRIMERO (recordar agregar la url despues)
    path('saludar2/', views.saludar_con_etiqueta), # 2° Y MOSTRAR (recordar agregar la url despues)
    path('saludar3/<str:nombre>/<str:apellido>', views.saludar_con_parametros), # 3° (recordar agregar la url despues y al mostrar ingresar los parametros ---> http://127.0.0.1:8000/saludar3/alan/ejemplo)´
    path('probandoTemplate/', views.probando_template),
    path('app/', include('AppCoder.urls')),

]

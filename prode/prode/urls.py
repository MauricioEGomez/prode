"""
URL configuration for prode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guardian.urls')),
    path('prodes/', views.prodes, name='prodes'),
    path('pronosticos/', views.pronosticos, name='pronosticos'),
    path('partidos/', views.partidos, name='partidos'),
    path('participantes/', views.participantes, name='participantes'),
    path('participantes/nuevo/', views.nuevo_participante, name='nuevo_participante'),
    path('prodes/nuevo/', views.nuevo_prode, name='nuevo_prode'),
    path('prodes/fechas/nueva/', views.nueva_fecha, name='nueva_fecha'),
    path('prodes/fechas/<int:concurso_id>/', views.fechas_prode, name='fechas_prode'),
    path('prodes/fechas/partidos/<int:fecha_id>/', views.partidos_fecha_prode, name='partidos_fecha_prode'),
    path('prodes/fechas/partido/<int:id>/', views.partido, name='partido'),
    path('prodes/fecha/<int:id>/', views.fecha_prode, name='fecha_prode'),
    path('prodes/fecha/pronostico/nuevo', views.nuevo_pronostico, name='nuevo_pronostico'),
]

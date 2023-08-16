from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('jugadores/', jugadores, name='jugadores'),
    path('clubes/', clubes, name='clubes'),
    path('ligas/', ligas, name='ligas'),
    path('formJugadores/', formJugadores, name='formJugadores'),
    path('formClubes/', formClubes, name='formClubes'),
    path('formLigas/', formLigas, name='formLigas'),
    path('jugadoresBuscar/', jugadores_buscar, name='jugadoresBuscar'),
    path('clubesBuscar/', clubes_buscar, name='clubesBuscar'),
    path('ligasBuscar/', ligas_buscar, name='ligasBuscar'),
]

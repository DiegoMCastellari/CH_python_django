from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    altura = models.IntegerField()
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    estado_actividad = models.BooleanField()

class Clubes(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    arena = models.CharField(max_length=100)
    liga = models.CharField(max_length=100)

class Ligas (models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)
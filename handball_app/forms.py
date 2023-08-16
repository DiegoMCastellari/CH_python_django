from django import forms 

class JugadoresForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=True)
    altura = forms.IntegerField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    nacionalidad = forms.CharField(max_length=100, required=True)
    club = forms.CharField(max_length=100, required=True)
    estado_actividad = forms.BooleanField(required=True)

class ClubesForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=True)
    ciudad = forms.CharField(max_length=100, required=True)
    pais = forms.CharField(max_length=100, required=True)
    arena = forms.CharField(max_length=100, required=True)
    liga = forms.CharField(max_length=100, required=True)

class LigasForm (forms.Form):
    nombre = forms.CharField(max_length=255, required=True)
    pais = forms.CharField(max_length=100, required=True)
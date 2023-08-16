from django.shortcuts import render
from .models import Jugador, Clubes, Ligas
from .forms import JugadoresForm, ClubesForm, LigasForm

# Create your views here.

def home(request):
    return render(request, "handball_app/home.html")

def jugadores(request):
    contexto = {'jugadores': Jugador.objects.all}
    return render(request, "handball_app/jugadores.html", contexto)

def jugadores_buscar(request):
    if request.GET['buscar']:
        filtro = request.GET['buscar']
        jugadores_filtrados = Jugador.objects.filter(nombre__icontains=filtro)
        contexto = {'jugadores': jugadores_filtrados, 'gotodiv': 'datos', 'filtro_ingresado': f"Filtro ingresado: {filtro}"}
        if len(jugadores_filtrados) > 0:
            contexto = {'jugadores': jugadores_filtrados, 'gotodiv': 'datos', 'filtro_ingresado': f"Filtro ingresado: {filtro}"}
        else:
            contexto = {'jugadores': jugadores_filtrados, 'gotodiv': 'datos', 'filtro_ingresado':'Ningún objeto cumple el filtro!!!'}
    else:
        contexto = {'jugadores': Jugador.objects.all, 'gotodiv': 'datos', 'filtro_ingresado':'Filtro no ingresado!!!'}
    return render(request, "handball_app/jugadores.html", contexto)

def clubes(request):
    contexto = {'clubes': Clubes.objects.all}
    return render(request, "handball_app/clubes.html", contexto)

def clubes_buscar(request):
    if request.GET['buscar']:
        filtro = request.GET['buscar']
        clubes_filtrados = Clubes.objects.filter(nombre__icontains=filtro)
        if len(clubes_filtrados) > 0:
            contexto = {'clubes': clubes_filtrados, 'gotodiv': 'datos', 'filtro_ingresado': f"Filtro ingresado: {filtro}"}
        else:
            contexto = {'clubes': clubes_filtrados, 'gotodiv': 'datos', 'filtro_ingresado':'Ningún objeto cumple el filtro!!!'}
    else:
        contexto = {'clubes': Clubes.objects.all, 'gotodiv': 'datos', 'filtro_ingresado':'Filtro no ingresado!!!'}
    return render(request, "handball_app/clubes.html", contexto)

def ligas(request):
    contexto = {'ligas': Ligas.objects.all}
    return render(request, "handball_app/ligas.html", contexto)

def ligas_buscar(request):
    if request.GET['buscar']:
        filtro = request.GET['buscar']
        ligas_filtrados = Ligas.objects.filter(nombre__icontains=filtro)
        if len(ligas_filtrados) > 0:
            contexto = {'ligas': ligas_filtrados, 'gotodiv': 'datos', 'filtro_ingresado': f"Filtro ingresado: {filtro}"}
        else:
            contexto = {'ligas': ligas_filtrados, 'gotodiv': 'datos', 'filtro_ingresado':'Ningún objeto cumple el filtro!!!'}
    else:
        contexto = {'ligas': Ligas.objects.all, 'gotodiv': 'datos', 'filtro_ingresado':'Filtro no ingresado!!!'}
    return render(request, "handball_app/ligas.html", contexto)

def formJugadores(request):
    if request.method == 'POST':
        miForm = JugadoresForm(request.POST)
        if miForm.is_valid():
            jugador_nombre = miForm.cleaned_data.get('nombre')
            jugador_altura = miForm.cleaned_data.get('altura')
            jugador_fecha_nacimiento = miForm.cleaned_data.get('fecha_nacimiento')
            jugador_nacionalidad = miForm.cleaned_data.get('nacionalidad')
            jugador_club = miForm.cleaned_data.get('club')
            jugador_estado_actividad = miForm.cleaned_data.get('estado_actividad')

            jugador = Jugador(
                nombre = jugador_nombre,
                altura = jugador_altura,
                fecha_nacimiento = jugador_fecha_nacimiento,
                nacionalidad = jugador_nacionalidad,
                club = jugador_club,
                estado_actividad = jugador_estado_actividad
            )
            jugador.save()
            
            contexto = {'jugadores': Jugador.objects.all}
            return render(request, "handball_app/jugadores.html", contexto)

    else:
        miForm = JugadoresForm()

    return render(request, "handball_app/formJugadores.html", {"form":miForm})

def formClubes(request):
    if request.method == 'POST':
        miForm = ClubesForm(request.POST)
        if miForm.is_valid():
            club_nombre = miForm.cleaned_data.get('nombre')
            club_ciudad = miForm.cleaned_data.get('ciudad')
            club_pais = miForm.cleaned_data.get('pais')
            club_arena = miForm.cleaned_data.get('arena')
            club_liga = miForm.cleaned_data.get('liga')

            club = Clubes(
                nombre = club_nombre,
                ciudad = club_ciudad,
                pais = club_pais,
                arena = club_arena,
                liga = club_liga
            )
            club.save()
            
            contexto = {'ligas': Ligas.objects.all}
            return render(request, "handball_app/clubes.html", contexto)

    else:
        miForm = ClubesForm()

    return render(request, "handball_app/formClubes.html", {"form":miForm})

def formLigas(request):
    if request.method == 'POST':
        miForm = LigasForm(request.POST)
        if miForm.is_valid():
            liga_nombre = miForm.cleaned_data.get('nombre')
            liga_pais = miForm.cleaned_data.get('pais')

            liga = Ligas(
                nombre = liga_nombre,
                pais = liga_pais
            )
            liga.save()
            
            contexto = {'ligas': Ligas.objects.all}
            return render(request, "handball_app/ligas.html", contexto)

    else:
        miForm = LigasForm()

    return render(request, "handball_app/formLigas.html", {"form":miForm})
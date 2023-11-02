from django.shortcuts import render
from .forms import Tablero


# Create your views here.
def inicio(request):
    return render(request, 'buscaminas/index.html', {})


def crea_tablero(request):
    # Se crea el objeto vacio para el formulario.
    table_form = Tablero()

    # Si se ha enviado el formulario.
    if request.method == 'POST':
        table_form_param = Tablero(request.POST)
    # Si se pide la página por primera vez.
    return render(request, 'buscaminas/crea_tablero.html', {'form': table_form})

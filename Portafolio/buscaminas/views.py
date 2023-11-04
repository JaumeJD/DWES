from django.shortcuts import render
from .forms import Tablero
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, 'buscaminas/index.html', {})


@csrf_exempt
def crea_tablero(request):
    # Se crea el objeto vacio para el formulario.
    table_form = Tablero()

    # Si se ha enviado el formulario.
    if request.method == 'POST':
        table_form_param = Tablero(request.POST)

        if table_form_param.is_valid():
            rows = int(request.POST['rows'])
            cols = int(request.POST['cols'])
            mines = int(request.POST['minas'])

            return render(request, 'buscaminas/muestraTablero.html',
                          {'filas': rows, 'rangoF': range(rows), 'minas': mines,
                           'columnas': cols, 'rangoC': range(cols), 'table': table_form_param})
    # Si se pide la página por primera vez.
    return render(request, 'buscaminas/crea_tablero.html', {'form': table_form})

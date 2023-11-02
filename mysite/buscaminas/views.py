from django.shortcuts import render
from .forms import CreaTablero


def index(request):
    return render(request, "index.html", {})


def crea_tablero(request):
    # Se crea el objeto vacio.
    table_form = CreaTablero()

    # Si se ha enviado el formulario.
    if request.method == 'GET':
        table_form_param = CreaTablero(request.GET)
        # Ejecutamos la validacion
        if table_form_param.is_valid():
            # Los datos se cogen del diccionario cleaned_data
            filas = table_form_param.cleaned_data['rows']
            columnas = table_form_param.cleaned_data['cols']

            return render(request, 'muestra_tablero.html', {'filas': filas,
                                                   'columnas': columnas, 'rango_filas': range(filas),
                                                       'rango_columnas': range(columnas), 'tablaparam': table_form_param})

    # Si se pide la página por primera vez.
    return render(request, 'crea_tablero.html', {'form': table_form})

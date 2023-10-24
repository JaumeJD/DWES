from django.shortcuts import render
from django.http import HttpResponse
from .forms import TableForm


def index(request):
    return render(request, "index.html")


def form_table(request):
    table_form = TableForm()
    table_form_param = TableForm(request.GET)

    if table_form_param.is_valid():

        filas = int(table_form_param.cleaned_data['rows'])
        columnas = int(table_form_param.cleaned_data['cols'])

        filasRange = range(filas)
        columnasRange = range(columnas)

        return render(request, 'form_table.html', {'filas': filasRange,
                                                   'columnas': columnasRange, 'tablaparam': table_form_param})
    else:

        return render(request, 'form_table.html', {'tabla': table_form})

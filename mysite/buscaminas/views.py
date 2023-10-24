from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

# def info_form(request):
#    if request.GET["filas"]:
#
#       valor = "Filas: %r\n" % request.GET["filas"],
#
#   else:
#
#       valor = "No has introducido ninguna fila",
#
#   return HttpResponse(valor)

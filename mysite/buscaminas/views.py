from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Soy Jaime y este será mi buscaminas.")


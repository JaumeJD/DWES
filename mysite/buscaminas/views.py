from django.shortcuts import render
from django.http import HttpResponse
from .forms import TableForm


def index(request):

    return render(request, "index.html")


def create_form(request):

    return render(request, "create_form.html")



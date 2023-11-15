from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import Formulario


def tu_vista(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            # Procesar el formulario
            # ...
            return redirect('alguna_vista_exitosa')
    else:
        # Setear la marca de tiempo cuando se carga el formulario
        form = Formulario(initial={'timestamp': timezone.now()})

    return render(request, 'tu_template.html', {'form': form})

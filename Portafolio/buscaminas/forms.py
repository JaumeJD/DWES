from django import forms


class Tablero(forms.Form):
    rows = forms.IntegerField(label='Filas:', min_value=1, max_value=20, initial=2, required=True)
    cols = forms.IntegerField(label='Columnas:', min_value=1, max_value=15, initial=2, required=True)

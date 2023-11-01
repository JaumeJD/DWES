from django import forms


class CreaTablero(forms.Form):
    rows = forms.IntegerField(label='Filas:', min_value=1, max_value=15, required=True, initial=2)
    cols = forms.IntegerField(label='Columnas:', min_value=1, max_value=15, required=True, initial=2)


from django import forms


class TableForm(forms.Form):
    rows = forms.CharField(label='Filas:', max_length=20)
    cols = forms.CharField(label='Columnas:', max_length=15)


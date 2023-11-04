from django import forms
from django.forms import Form


class Tablero(forms.Form):
    rows = forms.IntegerField(label='Filas:', min_value=1, max_value=20, initial=2, required=True)
    cols = forms.IntegerField(label='Columnas:', min_value=1, max_value=15, initial=2, required=True)
    minas = forms.IntegerField(label='Minas:', min_value=1, initial=1, required=True)

    def clean_minas(self):
        cleaned_data = self.cleaned_data
        rows = cleaned_data.get('rows')
        cols = cleaned_data.get('cols')
        minas = cleaned_data.get('minas')

        if minas > (rows * cols) // 2:
            self.add_error('minas', forms.ValidationError('ASDASDASDASDASD'))

        return cleaned_data

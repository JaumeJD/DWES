from django import forms


class TableForm(forms.Form):
    rows = forms.CharField(label='Rows', max_length=20),
    cols = forms.CharField(label='Cols', max_length=15),


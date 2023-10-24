from django import forms


class TableForm(forms.Form):
    row = forms.CharField(label='Rows', max_length=20),
    col = forms.CharField(label='Cols', max_length=20),


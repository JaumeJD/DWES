import re
from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError


class Formulario(forms.Form):
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    dias_semana = forms.DateField(label="Fecha de nacimiento", required=True,
                                  widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
                                  input_formats=["%Y-%m-%d"])
    email = forms.EmailField()

    def clean_fecha_fin(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')

        if fecha_fin < fecha_inicio:
            raise forms.ValidationError('La fecha de finalización debe ser igual o posterior a la fecha de inicio.')

        return fecha_fin

    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')

        if not correo_electronico.endswith('@iesmartinezm.es'):
            raise forms.ValidationError('El correo electrónico debe terminar con @iesmartinezm.es')

        return correo_electronico

    def clean_dias_semana(self):
        dias_semana = self.cleaned_data.get('dias_semana').split(',')
        if not dias_semana:
            raise forms.ValidationError('Debe seleccionar al menos un día de la semana.')

        if len(dias_semana) > 3:
            raise forms.ValidationError('No se pueden seleccionar más de 3 días de la semana.')

        return self.cleaned_data.get('dias_semana')

    def es_contenido(nombre_usuario, contraseña):
        return nombre_usuario.lower() in contraseña.lower()

    # return self.upper() in contraseña.upper()
    # Subcadena in cadena
    # Tambien puede funcionar con cadena.find(subcadena)

    nombre_usuario = "usuario"
    contraseña = "miUsuario123"

    if es_contenido(nombre_usuario, contraseña):
        print("La contraseña contiene el nombre de usuario.")
    else:
        print("La contraseña NO contiene el nombre de usuario.")

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')

        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', contrasena):
            raise ValidationError(
                'La contraseña debe tener al menos 8 caracteres, incluyendo al menos una letra mayúscula, una letra '
                'minúscula, un número y un caracter especial.'
            )

        return contrasena

    def clean_timestamp(self):
        timestamp = self.cleaned_data.get('timestamp')
        now = datetime.now()

        if timestamp and (now - timestamp).seconds > 120:
            raise ValidationError('El formulario ha caducado. Por favor, recárguelo y envíelo nuevamente.')

        return timestamp

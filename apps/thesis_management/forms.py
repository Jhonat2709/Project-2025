from django import forms
from django.core.validators import RegexValidator
from apps.core.models import (
    Periodos,
    Tesis,
    PalabrasClave,
    TesisPalabrasClave,
    Carreras
)
# Formularios para la gestión de tesis.


class TesisForm(forms.ModelForm):


    # Definición del input para el periodo académico.
    class Meta:
        model = Tesis
        fields = [
            "titulo",
            "resumen",
            "carrera",
            "documento",
        ]
        widgets = {
            "resumen": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }

    def save(self, commit=True):
        return super().save(commit=commit)


# TEST: Lista para testear.


class UploadFileForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=True, label="Título")
    resumen = forms.CharField(max_length=5000, required=True, label="Resumen")
    file = forms.FileField(required=True, label="Archivo")
    # WARNING: Clase inutilizada, pero se deja por si se necesita en el futuro.

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = [
            'nombre',
        ]
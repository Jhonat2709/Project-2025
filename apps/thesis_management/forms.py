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
    # Definición del input para palabras clave.
    palabras_clave_texto = forms.CharField(
        label="Palabras Clave (separadas por coma)",
        widget=forms.Textarea(attrs={"rows": 2}),
        required=True,
        help_text="Ejemplo: inteligencia artificial, machine learning, python",
    )

    # Definición del input para el periodo académico.
    periodo_academico = forms.CharField(
        label="Período Académico",
        max_length=6,
        required=True,
        help_text="Ejemplo: I-2025 o II-2025",
        validators=[  # NOTE: Esta lista para definir validaciones del lado del servidor hay que testearlas y ver si funciona en un futuro.
            RegexValidator(
                regex=r"^(I|II)-\d{4}$",
                message="El formato debe ser I-AAAA o II-AAAA (ej: I-2025)",
                code="invalid_periodo",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "pattern": r"^(I|II)-\d{4}$",
                "title": "Formato: I-AAAA o II-AAAA (ej: I-2025)",
            }
        ),
    )

    class Meta:
        model = Tesis
        fields = [
            "titulo",
            "resumen",
            "numero_paginas",
            # "periodo_academico", #NOTE: Campo comentado, por si se puede usar luego.
            "carrera",
            "documento",
        ]
        widgets = {
            "resumen": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }

    def save(self, commit=True):
        """
        Guardamos la instancia de Tesis y luego procesamos las palabras clave.
        NOTA: La lógica de los autores se moverá a la vista.
        """
        # Obtención del texto del formulario para el periodo académico
        periodo = self.cleaned_data.get("periodo_academico", "")
        # Buscar o crear el objeto Periodos
        periodo_obj, created = Periodos.objects.get_or_create(nombre=periodo)

        # Guardamos la tesis principal
        tesis_instance = super().save(commit=False)
        # Asignar el periodo académico ANTES de guardar
        tesis_instance.periodo_academico = periodo_obj

        tesis_instance = super().save(commit=commit)
        if commit:
            # Lógica para Palabras Clave

            # Obtención del texto del formulario
            keywords_string = self.cleaned_data.get("palabras_clave_texto", "")

            # División del string por comas y procesamos cada palabra
            keyword_list = [
                kw.strip() for kw in keywords_string.split(",") if kw.strip()
            ]

            for palabra in keyword_list:
                # get_or_create: busca la palabra clave. Si no existe, la crea.
                # Devuelve el objeto y un booleano 'created'.
                kw_obj, created = PalabrasClave.objects.get_or_create(
                    palabra=palabra.lower()  # Guardamos en minúsculas para evitar duplicados
                )

                # Creamos la relación en la tabla puente
                TesisPalabrasClave.objects.create(
                    tesis=tesis_instance, palabras_clave=kw_obj
                )

        return tesis_instance


# TEST: Lista para testear.


class UploadFileForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=True, label="Título")
    numero_paginas = forms.CharField(
        max_length=4, required=True, label="Número de páginas"
    )
    resumen = forms.CharField(max_length=5000, required=True, label="Resumen")
    palabras_clave = forms.CharField(
        max_length=50, required=True, label="Palabras clave"
    )
    periodo = forms.CharField(max_length=100, required=True, label="Período")
    file = forms.FileField(required=True, label="Archivo")
    # WARNING: Clase inutilizada, pero se deja por si se necesita en el futuro.

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = [
            'nombre',
        ]
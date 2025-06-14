from django import forms
from .models import Tesis, Autores, PalabrasClave, Periodos, Categoria

class TesisForm(forms.ModelForm):
    resumen = forms.CharField(widget=forms.Textarea, required=False)
    carrera = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Seleccione una categoría")

    class Meta:
        model = Tesis
        fields = ['resumen', 'titulo', 'carrera', 'documento', 'numero_paginas']
        widgets = {
            'numero_paginas': forms.NumberInput(attrs={'placeholder': 'Ingrese el número de páginas'}),
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nombres', 'apellidos']

class PalabrasClaveForm(forms.ModelForm):
    class Meta:
        model = PalabrasClave
        fields = ['palabra']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
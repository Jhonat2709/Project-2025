from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .utils import ultima_tesis_carreras
from django.contrib.auth.decorators import login_required
from .decorators import login_excluded
from .models import Tesis, Categoria
import os
from haystack.views import SearchView

class CustomSearchView(SearchView):
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('carrera')
        if categoria_id:
            try:
                categoria = Categoria.objects.get(id=categoria_id)
                queryset = queryset.filter(carrera=categoria.nombre)
            except Categoria.DoesNotExist:
                pass # Handle invalid category ID gracefully
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        ultima_tesis_por_carrera = ultima_tesis_carreras.obtener_ultimas_tesis_por_carrera()
        context['ultima_tesis_carrera'] = ultima_tesis_por_carrera
        context['carreras'] = Categoria.objects.all()
        return context

def dashboard(request):

    ultima_tesis_por_carrera = ultima_tesis_carreras.obtener_ultimas_tesis_por_carrera()
    return render(request, 'core/dashboard.html', {'ultima_tesis_carrera': ultima_tesis_por_carrera})

@login_excluded('dashboard')
def signin(request):
    return render(request, 'core/login.html')

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))

def tesis_detail(request, tesis_id):
    tesis = get_object_or_404(Tesis, id=tesis_id)
    palabras_clave = [tesis_palabras_clave.palabras_clave for tesis_palabras_clave in tesis.tesispalabrasclave_set.all()]
    autores = [relacion.autor for relacion in tesis.tesisautores_set.all()]
    
    context = {
        'tesis': tesis, 
        'palabras_clave': palabras_clave,
        'autores': autores,
    }

    return render(request, 'core/tesis_detail.html', context)

def descargar_tesis(request, tesis_id):
    try:
        tesis = Tesis.objects.get(id=tesis_id)
        file_path = tesis.documento.path
        print(file_path)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    except Tesis.DoesNotExist:
        raise Http404("Archivo no encontrado")

from .forms import TesisForm, AutorForm, PalabrasClaveForm
from .models import Carreras
from django.shortcuts import render, redirect, get_object_or_404
from .models import TesisAutores, TesisPalabrasClave, Autores, PalabrasClave

@login_required
def cargar_tesis(request):
    if request.method == 'POST':

        tesis_form = TesisForm(request.POST, request.FILES)
        autor_form = AutorForm(request.POST)
        palabras_clave_form = PalabrasClaveForm(request.POST)

        if tesis_form.is_valid():
            print("Tesis form is valid.")
            tesis = tesis_form.save(commit=False)
            tesis.numero_paginas = tesis_form.cleaned_data.get('numero_paginas')
            tesis.save()
            print(f"Tesis saved with ID: {tesis.id}")

            autores_nombres_str = request.POST.get('autores_nombres', '').strip()
            if not autores_nombres_str:
                messages.error(request, 'El campo Autores es obligatorio.')
                return render(request, 'core/cargar_tesis.html', {'tesis_form': tesis_form, 'autor_form': autor_form, 'palabras_clave_form': palabras_clave_form})

            autores_nombres = autores_nombres_str.split(',')
            for nombre_completo in autores_nombres:
                nombres_apellidos = nombre_completo.strip().split(' ', 1)
                nombres = nombres_apellidos[0] if len(nombres_apellidos) > 0 else ''
                apellidos = nombres_apellidos[1] if len(nombres_apellidos) > 1 else ''
                autor, created = Autores.objects.get_or_create(nombres=nombres, apellidos=apellidos)
                TesisAutores.objects.create(tesis=tesis, autor=autor)

            palabras_clave_str_input = request.POST.get('palabras_clave_palabra', '').strip()
            if not palabras_clave_str_input:
                messages.error(request, 'El campo Palabras Clave es obligatorio.')
                return render(request, 'core/cargar_tesis.html', {'tesis_form': tesis_form, 'autor_form': autor_form, 'palabras_clave_form': palabras_clave_form})

            palabras_clave_list = palabras_clave_str_input.split(',')
            for palabra_str in palabras_clave_list:
                palabra, created = PalabrasClave.objects.get_or_create(palabra=palabra_str.strip())
                TesisPalabrasClave.objects.create(tesis=tesis, palabras_clave=palabra)

            messages.success(request, '¡Tesis cargada exitosamente!')
            return redirect('dashboard') # Redirect to a success page or dashboard
        else:
            print("Tesis Form Errors:", tesis_form.errors)
            messages.error(request, 'Por favor, corrija los errores en el formulario de la tesis.')
    else:


        tesis_form = TesisForm()
        autor_form = AutorForm()
        palabras_clave_form = PalabrasClaveForm()

    categorias = Categoria.objects.all()

    context = {
        'tesis_form': tesis_form,
        'autor_form': autor_form,
        'palabras_clave_form': palabras_clave_form,
        'categorias': categorias,
    }
    return render(request, 'core/cargar_tesis.html', context)

from .forms import CategoriaForm

@login_required
def categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría añadida exitosamente!')
            return redirect('categorias')
        else:
            messages.error(request, 'Error al añadir la categoría. Por favor, revise los campos.')
    else:
        form = CategoriaForm()

    categorias_list = Categoria.objects.all()
    context = {
        'categorias': categorias_list,
        'form': form,
    }
    return render(request, 'core/categorias.html', context)
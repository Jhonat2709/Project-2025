from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .utils import ultima_tesis_carreras, Object_models
from django.contrib.auth.decorators import login_required
from .decorators import login_excluded
from .models import Tesis, TesisPalabrasClave
import os

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
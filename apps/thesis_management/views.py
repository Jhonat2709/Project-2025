from django.shortcuts import render
from .forms import UploadFileForm, TesisForm, CarreraForm
from apps.core.models import Carreras, Autores, TesisAutores


def crear_tesis_view(request):
    if request.method == "POST":
        # Pasamos request.POST y request.FILES al formulario
        form = TesisForm(request.POST, request.FILES)

        if form.is_valid():
            # 1. Guardar el formulario. Esto crea la Tesis y maneja las Palabras Clave.
            # commit=True es el default, pero lo dejamos explícito para claridad.
            # Nuestro método save() modificado se ejecutará aquí.
            tesis_obj = form.save(commit=True)

            # 2. Procesar los autores desde request.POST
            # Creamos un diccionario para agrupar nombres y apellidos por su índice
            autores_data = {}
            for key, value in request.POST.items():
                if key.startswith("autor_nombres_"):
                    index = key.split("_")[-1]
                    if index not in autores_data:
                        autores_data[index] = {}
                    autores_data[index]["nombres"] = value
                elif key.startswith("autor_apellidos_"):
                    index = key.split("_")[-1]
                    if index not in autores_data:
                        autores_data[index] = {}
                    autores_data[index]["apellidos"] = value

            # 3. Iterar sobre los datos de autores agrupados y crearlos
            for index, data in autores_data.items():
                nombres = data.get("nombres", "").strip()
                apellidos = data.get("apellidos", "").strip()

                # Solo crear el autor si ambos campos tienen valor
                if nombres and apellidos:
                    # Siempre creamos un nuevo autor según tu requerimiento
                    nuevo_autor = Autores.objects.create(
                        nombres=nombres, apellidos=apellidos
                    )
                    # Creamos la relación en la tabla puente
                    TesisAutores.objects.create(tesis=tesis_obj, autor=nuevo_autor)
    else:
        form = TesisForm()

    return render(request, "upload_thesis.html", {"form": form, "carreras" : Carreras.objects.all() })


""" def UploadFileView(request):
    if request.method == "GET":
        carreras = Carreras.objects.all()
        form = UploadFileForm()
        return render(
            request,
            "upload_thesis.html",
            {"form": form, "carreras": carreras},
        )
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            print(titulo)
            autores = form.cleaned_data["autores"]
            print(autores)
            numero_paginas = form.cleaned_data["numero_paginas"]
            print(numero_paginas)
            resumen = form.cleaned_data["resumen"]
            print(resumen)
            periodo = form.cleaned_data["periodo"]
            print(periodo)
            carrera = request.POST.get("carreras")
            print(carrera)
            file = form.cleaned_data["file"]
            print(file)

        return render(request, "upload_thesis.html", {"form": form})"""

def upload_career(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            return render(request, 'upload_career.html', { 'error' : 'Datos inválidos' })
    else:
        form = CarreraForm()

    return render(request, 'upload_career.html', { 'form' : form })

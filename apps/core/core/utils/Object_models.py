from datetime import date
from core.models import Tesis, Periodos, Carreras, Autores, PalabrasClave, TesisAutores, TesisPalabrasClave 
import os
from django.core.files import File

def create_tesis():
    # Ruta del archivo en tu sistema
    file_path = os.path.join('media', 'thesis', 'digiciencia_vol7ArticuloYair.pdf')

    # Crea o recupera las instancias necesarias
    periodo = Periodos.objects.create(nombre='2022-1') 
    carrera = Carreras.objects.create(nombre='Ingeniería en Sistemas') 
    autor = Autores.objects.create(nombres='Yair Ricardo', apellidos='Córdoba Mosquera')  
    palabra_clave = PalabrasClave.objects.create(palabra='Tecnología')  

    # Crea la instancia de Tesis
    tesis = Tesis(
        resumen='Esta es una tesis sobre el aula invertida en entornos enriquecidos por tecnología.',
        titulo='Principios de diseño del aula invertida en entorno enriquecido por tecnología',
        fecha_publicacion=date.today(),
        numero_paginas=36,  
        periodo_academico=periodo,
        carrera=carrera,
        estado=True
    )

    # Abre el archivo y guárdalo en el campo documento
    with open(file_path, 'rb') as f:
        tesis.documento.save('digiciencia_vol7ArticuloYair.pdf', File(f))

    tesis.save()  # Guarda la instancia de Tesis

    # Agregar autores y palabras clave
    TesisAutores.objects.create(tesis=tesis, autor=autor)
    TesisPalabrasClave.objects.create(tesis=tesis, palabras_clave=palabra_clave)

    return print("Tesis creada con éxito:", tesis)

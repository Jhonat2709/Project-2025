
from core.models import Carreras, Tesis, TesisAutores
def obtener_ultimas_tesis_por_carrera():

    # Obtener todas las carreras
    carreras = Carreras.objects.all()
    resultados = []
    for carrera in carreras:
        # Obtener la última tesis publicada para la carrera actual
        ultima_tesis = Tesis.objects.filter(carrera=carrera).order_by('-fecha_publicacion').first()
        
        if ultima_tesis:
            # Obtener los autores de la tesis
            autores = TesisAutores.objects.filter(tesis=ultima_tesis).select_related('autor')
            autores_nombres = [f"{autor.autor.nombres} {autor.autor.apellidos}" for autor in autores]
            resultados.append({
                'id_tesis': ultima_tesis.id,
                'titulo': ultima_tesis.titulo,
                'carrera': carrera.nombre,
                'autores': ', '.join(autores_nombres),
                'fecha_publicacion': ultima_tesis.fecha_publicacion,
            })
    
    return resultados
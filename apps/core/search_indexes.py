from haystack import indexes
from apps.core.models import Tesis

class TesisIndex(indexes.SearchIndex, indexes.Indexable):
    # Campo principal de búsqueda que usa el template
    text = indexes.CharField(document=True, use_template=True)
    
    # Campos adicionales para búsquedas específicas
    titulo = indexes.CharField(model_attr='titulo')
    resumen = indexes.CharField(model_attr='resumen')
    carrera = indexes.CharField(model_attr='carrera__nombre')
    palabras_clave = indexes.CharField()

    def get_model(self):
        return Tesis
    
    def prepare_palabras_clave(self, obj):
        # Obtener todas las palabras clave asociadas a esta tesis
        palabras = obj.tesispalabrasclave_set.select_related('palabras_clave').all()
        return " ".join([tc.palabras_clave.palabra for tc in palabras])
    
    def index_queryset(self, using=None):
        # Solo indexar tesis activas
        return self.get_model().objects.select_related('carrera').prefetch_related(
            'tesispalabrasclave_set__palabras_clave',
            'tesisautores_set__autor'
        ).filter(estado=True)

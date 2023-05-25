import django_filters
from apps.documentos.models import TipoDocumentos

class TipoDocumentosFilterSet(django_filters.FilterSet):
    class Meta:
        model = TipoDocumentos
        fields = ['codigo', 'abreviatura', 'flag', 'descripcion']

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from apps.documentos.models import TipoDocumentos
from apps.documentos.filters import TipoDocumentosFilterSet
from .serializers import TipoDocumentoSerializer
from .. import constants 

class TipoDocumentoList(generics.ListAPIView):
    authentication_classes = []
    serializer_class = TipoDocumentoSerializer
    queryset = TipoDocumentos.objects.filter(
        codigo__in=(
            constants.TIPO_DOCUMENTO_DNI,
            constants.TIPO_DOCUMENTO_CE,
            constants.TIPO_DOCUMENTO_CPP,
        )
    ).order_by('codigo')
    http_method_names = ['get',]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TipoDocumentosFilterSet
    search_fields = ['codigo','abreviadura','flag']
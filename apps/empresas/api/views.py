import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from apps.empresas.models import TipoContribu,TamanoEmpresa
from apps.empresas.filters import TipoContribuFilterSet
from .serializers import (TipoContribuSerializer,TamanoEmpresaSerializer)
from apps.documentos import constants

class TipoContribuyenteList(generics.ListAPIView):
   authentication_classes = []    
   serializer_class = TipoContribuSerializer
   queryset = TipoContribu.objects.filter(
      codigo__in=(
         constants.TIPO_CONTRI_SA_A,
         constants.TIPO_CONTRI_PERSONA_NATURAL_C,
         constants.TIPO_CONTRI_EIRL,
         constants.TIPO_CONTRI_SA,
         constants.TIPO_CONTRI_SA_C
      )
   )

class TamanoEmpresaList(generics.ListAPIView):
   authentication_classes = [] 
   serializer_class = TamanoEmpresaSerializer
   queryset = TamanoEmpresa.objects.filter()
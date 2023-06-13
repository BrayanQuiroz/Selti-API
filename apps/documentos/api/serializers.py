from rest_framework import serializers

from apps.documentos.models import TipoDocumentos

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentos
        fields = ['codigo', 'descripcion', 'abreviatura', 'flag']